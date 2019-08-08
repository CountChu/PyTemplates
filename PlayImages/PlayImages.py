#
# FILENAME.
#       PlayImages.py - Play Images Application.
#
# FUNCTIONAL DESCRIPTION.
#       The app plays images or video optionally step by step. The app is also 
#       a template. We can modify it for specific purpose of computer vision.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/6/3
#

#
# Include standard packages.
#

import argparse
import logging
import pdb
import datetime
import time
import cv2
import os
import json

#
# Include specific packages.
#

import Video

#
# Build argument parser and return it.
#
    
def buildArgParser():

    desc = '''
The app plays images or video optionally step by step.

Usage 1: python PlayImages.py --images Test1 --step
    Play images in the directory Test1 step by step
    
Usage 2: python PlayImages.py --images Test1 --fps -r
    Play images in the directory Test1 with FPS and combined them in a video out.mp4.

Usage 3: python PlayImages.py --fps -r
    Open camera with FPS and save frames in out.mp4.     
    
Usage 4: python PlayImages.py --video Test1.mp4 --ri Output
    Play the video Test1.mp4. You can modify the app to handle the video, 
    and output the result images in the directory Output.        
'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Standard arguments
    #
                
    parser.add_argument(
            "-v", 
            dest="verbose", 
            action='store_true',    
            help="Verbose log") 
            
    #
    # Anonymous arguments.
    #
       
    #
    # Specific arguments
    #     
    
    parser.add_argument(
            "--video", 
            dest="videoFn",
            help="A path to the video file") 

    parser.add_argument(
            '--images',
            dest='imagesDir',
            help='A directory that contains images') 
            
    parser.add_argument(
            "--begin", 
            dest="beginNum", 
            type=int,
            default=0,
            help="Begin of the images")        
            
    parser.add_argument(
            "--end", 
            dest="endNum", 
            type=int,
            help="End of the images")               

    parser.add_argument(
            "--step", 
            dest="step", 
            action='store_true',    
            help="Enable step. Press '>.' for next step and '<,' for previous step")  

    parser.add_argument(
            "--goto", 
            dest="gotoNum", 
            type=int,
            help="The argument follows --step.")              

    parser.add_argument(
            "-r", 
            dest="record", 
            action='store_true',   
            help="Record video.")

    parser.add_argument(
            '--log',
            dest='logFn',
            help='A name of a log file.')              

    parser.add_argument(
            "--ri", 
            dest="recordImagesDir", 
            help="A directory where images are recorded")            

    parser.add_argument(
            "--fps", 
            dest="fps", 
            action='store_true',    
            help="Display fps.")          

    parser.add_argument(
            "--bn", 
            dest="basename", 
            action='store_true',    
            help="Display base name.")    

    parser.add_argument(
            "--sd", 
            dest="slowdown", 
            type=int,
            default=0,
            help="It follows -r. It slows down the output video by specifying a number of repeated frames")             
       
    return parser
    
def readConfig(jsonFn):   
    if not os.path.exists(jsonFn):
        return None

    f = open(jsonFn, 'r')
    lines = f.readlines()
    jsonStr = ''.join(lines)
    jsonObj = json.loads(jsonStr)
    f.close()
    
    return jsonObj    

def dispatchKey(key, step, video):

    #
    # If the 'q' key is pressed, break from the lop
    #

    if key == ord("q"):
        return False

    #
    # If step, apply  '<,' for previous and '>.' for next
    #
    
    if step:

        if key in [ord('>'), ord('.')]: # next
            video.next()    
    
        elif key in [ord('<'), ord(',')]: # previous
            video.previous()    
        
    return True
   
def main():      

    #
    # Parse arguments
    #
    
    args = buildArgParser().parse_args()
    
    #
    # Enable log if -v
    #
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)    

    #
    # Check arguments.
    #
    
    if args.videoFn is not None and args.imagesDir is not None:
        print ('Error. Arguments are wrong.')
        sys.exit(0)
        
    #
    # Open log file if --log
    #
    
    if args.logFn != None:
        logF = open(args.logFn, 'w')
        
    #
    # Read config.
    #
    
    jsonFn = 'DetectMotion.json'
    jsonObj = readConfig(jsonFn)
    
    #
    # Override args
    #
    
    if jsonObj != None:
        if 'imagesDir' in jsonObj['dataSet']:
            args.imagesDir = jsonObj['dataSet']['imagesDir']
            print('Override imagesDir = %s' % args.imagesDir)
    
    #
    # Create a video object.
    #
    
    video = Video.Video()
    
    #
    # Load a video file if --video
    #
    
    if args.videoFn is not None:
        print('Load a video file from %s.' % args.videoFn)
        video.loadVideoFile(args.videoFn)
        
    #
    # Load image files if --images
    #
        
    if args.imagesDir is not None:
        print('Load image files from %s.' % args.imagesDir)
        video.loadImageFiles(args.imagesDir, args.beginNum, args.endNum)
        
    #pdb.set_trace()
        
    #
    # Open camera if --video and --images are not specified.
    #
        
    if args.videoFn is None and args.imagesDir is None:
        print('Open the camera.')
        video.openCamera()
        
    #
    # Build VideoWriter if -r.
    #

    if args.record:
        outFileName = 'out.mp4'
        vw = None
        
    #
    # Variables of FPS if --fps
    #
    
    if args.fps:
        startTime = datetime.datetime.now()
        numFrames = 0
    
    #   
    # loop over the frames of the video
    #

    while True:

        line = '----------------------------------------------------------- video.num = %d ' % video.num
        logging.info(line)
        if args.logFn != None:
            logF.write(line+'\n')    
    
        #
        # grab the current frame and initialize the occupied/unoccupied
        # text
        #
        
        if args.step:
            if args.gotoNum is None:
                (grabbed, frame) = video.currentFrame()
            else:
                if video.num >= args.gotoNum:
                    (grabbed, frame) = video.currentFrame()
                else:
                    (grabbed, frame) = video.nextFrame()
        else:
            (grabbed, frame) = video.nextFrame()
            
        #
        # if the frame could not be grabbed, then we have reached the end
        # of the video
        #

        if not grabbed:
            break

        text = ''
            
        #    
        # Calculate Frames per second (FPS) if --fps
        #
        
        if args.fps:
            elapsedTime = (datetime.datetime.now() - startTime).total_seconds()
            fps = video.num / elapsedTime
            text += 'FPS: %d, Num: %d, ' % (int(fps), video.num)
            
        if args.basename:
            text += 'Name: %s, ' % os.path.basename(video.imgFnDict[video.num])
        if text[-2: ] == ', ':
            text = text[0:-2]
            
        #
        # Show video.num
        #
        
        if args.fps:
            cv2.putText(
                frame, 
                text, 
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.75,
                (0, 0, 255), 
                2)

        #
        # show the frame
        #
        
        cv2.imshow("Frame", frame)
        
        #
        # Record the frame in a video if -r
        #
        
        if args.record:
            if vw == None:
                vw = Video.videoWriter(frame, outFileName)
            vw.write(frame)    
            for i in range(args.slowdown):
                vw.write(frame)
            
        #
        # Record the frame in a image if --ri
        #
        
        if args.recordImagesDir != None:
            if not os.path.exists(args.recordImagesDir):
                print('Create %s' % args.recordImagesDir)
                os.mkdir(args.recordImagesDir)
            fn = '%s/%04d.jpg' % (args.recordImagesDir, video.num)
            print('Write %s' % fn)
            cv2.imwrite(fn, frame)
        
        #
        # Read a key.
        # 

        step = False
        if args.step:
            if args.gotoNum is None:
                key = cv2.waitKey(0)
                step = True
            else:
                if video.num >= args.gotoNum:
                    key = cv2.waitKey(0)
                    step = True
                else:
                    key = cv2.waitKey(1)  
        else:    
            key = cv2.waitKey(1)  
               
        #
        # Dispatch key.
        #
        
        if not dispatchKey(key, step, video):
            break
            

    #
    # cleanup the camera and close any open windows
    #

    video.close()
    cv2.destroyAllWindows()
    if args.record:
        print('Write %s.' % outFileName)
        vw.release()
        
    if args.logFn != None:
        logF.close()

main()