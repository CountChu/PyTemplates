#
# FILENAME.
#       PlayImages.py - Play Images Application.
#
# FUNCTIONAL DESCRIPTION.
#       The app plays images or video optionally step by step. The app is also
#       a template. We can modify it to develop applications of computer vision.
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
import sys
import re

#
# Include specific packages.
#

import plyimg.util as util
import plyimg.core as core
import plyimg.video

#
# Build argument parser and return it.
#

def build_args():

    desc = '''
The app plays images or video optionally step by step.

Usage 1: python -m plyimg --video TestVideo/video.MP4 --step
    Play the video file step by step.

Usage 2: python -m plyimg --video TestVideo/video.MP4 --ri TestImages
    Play the video file and save frames in the TestImages directory.

Usage 3: python -m plyimg --images TestImages --step
    Play images in the directory TestImages step by step.

Usage 4: python -m plyimg --images TestImages --fps -r
    Play images in the directory TestImages with FPS and combined them in a
    video out.mp4.

Usage 5: python -m plyimg --images TestImages --step -t
    Play images in the directory TestImages step by step and transform each
    frame by calling Util.transform(). You can modify the function to develop
    your specific application of computer vision.

Usage 6: python -m plyimg --fps -r
    Open camera with FPS and save frames in out.mp4.
'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Standard arguments
    #

    parser.add_argument(
            "--verbose",
            dest="verbose",
            action='store_true',
            help="Verbose log")

    parser.add_argument(
            "--debug",
            dest="debug",
            action='store_true',
            help="Show debug messages")

    parser.add_argument(
            '--log',
            dest='log_fn',
            help='A name of a log file.')

    parser.add_argument(
            '--cfg',
            action='store_true',
            help="Import Config.py")

    #
    # Anonymous arguments.
    #

    #
    # Specific arguments
    #

    parser.add_argument(
            "--video",
            dest="video_fn",
            help="A path to the video file")

    parser.add_argument(
            '--images',
            dest='images_dir',
            help='A directory that contains images')

    parser.add_argument(
            "--begin",
            dest="begin_num",
            type=int,
            default=0,
            help="Begin of the images")

    parser.add_argument(
            "--end",
            dest="end_num",
            type=int,
            help="End of the images")

    parser.add_argument(
            "--step",
            dest="step",
            action='store_true',
            help="Enable step. Press '>.' for next step and '<,' for previous step")

    parser.add_argument(
            "--goto",
            dest="goto_num",
            type=int,
            help="The argument follows --step.")

    parser.add_argument(
            "-r",
            dest="record",
            action='store_true',
            help="Record video.")

    parser.add_argument(
            "--ri",
            dest="record_images_dir",
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

    parser.add_argument(
            "-t",
            dest="transform",
            action='store_true',
            help="Enable transformation.")

    return parser.parse_args()

#
# It load Config.py
#

def read_config():

    pattern = "\<module\s\\'(.+)\\'\sfrom"
    text = str(sys.modules[__name__])
    logging.info('text = %s' % text)
    res = re.match(pattern, text)
    #pdb.set_trace()
    name = res.group(1)

    from config import config
    return config[name]

def dispatch_key(key, step, v):

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
            v.next()

        elif key in [ord('<'), ord(',')]: # previous
            v.previous()

    return True

def main():

    #
    # Parse arguments
    #

    args = build_args()

    #
    # Enable log if -v
    #

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)

    #
    # Enable verbose messages if --verbose
    #

    if args.verbose:
        print('.............verbose..............')

    #
    # Check arguments.
    #

    if args.video_fn is not None and args.images_dir is not None:
        print ('Error. Arguments are wrong.')
        sys.exit(0)

    #
    # Open a log file if --log
    #

    if args.log_fn != None:
        log_f = open(args.log_fn, 'w')

    #
    # If --cfg, specify default values if args don't exist.
    #

    if args.cfg:
        config = read_config()

        #
        # Override args
        #

        util.set_default_arg(config, args, '--video', 'video_fn')
        util.set_default_arg(config, args, '--ri', 'record_images_dir')

        util.set_config(config)

    #
    # Create a video object.
    #

    v = video.Video()

    #
    # Load a video file if --video
    #

    if args.video_fn is not None:
        print('Load a video file from %s.' % args.video_fn)
        v.load_video_file(args.video_fn)

    #
    # Load image files if --images
    #

    if args.images_dir is not None:
        print('Load image files from %s.' % args.images_dir)
        v.load_image_files(args.images_dir, args.begin_num, args.end_num)

    #pdb.set_trace()

    #
    # Open camera if --video and --images are not specified.
    #

    if args.video_fn is None and args.images_dir is None:
        print('Open the camera.')
        v.open_cam()

    #
    # Build VideoWriter if -r.
    #

    if args.record:
        out_fn = 'out.mp4'
        vw = None

    #
    # Variables of FPS if --fps
    #

    if args.fps:
        start_time = datetime.datetime.now()
        num_frames = 0

    #
    # loop over the frames of the video
    #

    while True:

        line = '----------------------------------------------------------- v.num = %d ' % v.num
        logging.info(line)
        if args.log_fn != None:
            log_f.write(line+'\n')

        #
        # grab the current frame and initialize the occupied/unoccupied
        # text
        #

        if args.step:
            if args.goto_num is None:
                (grabbed, frame) = v.cur_frame()
            else:
                if v.num >= args.goto_num:
                    (grabbed, frame) = v.cur_frame()
                else:
                    (grabbed, frame) = v.next_frame()
        else:
            (grabbed, frame) = v.next_frame()

        #
        # if the frame could not be grabbed, then we have reached the end
        # of the video
        #

        if not grabbed:
            break

        #
        # Declare text for displaying
        #

        text = ''

        #
        # Calculate Frames per second (FPS) if --fps
        #

        if args.fps:
            elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
            fps = v.num / elapsed_time
            text += 'FPS: %d, Num: %d, ' % (int(fps), v.num)

        if args.basename:
            text += 'Name: %s, ' % os.path.basename(v.img_fn_dict[v.num])
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
        # Transform the frame if -t.
        #

        if args.transform:
            core.transform(frame)

        #
        # show the frame
        #

        cv2.imshow("Frame", frame)

        #
        # Record the frame in a video if -r
        #

        if args.record:
            if vw == None:
                vw = video.video_writer(frame, out_fn)
            vw.write(frame)
            for i in range(args.slowdown):
                vw.write(frame)

        #
        # Record the frame in a image if --ri
        #

        if args.record_images_dir != None:
            if not os.path.exists(args.record_images_dir):
                print('Create %s' % args.record_images_dir)
                os.mkdir(args.record_images_dir)
            fn = '%s/%04d.jpg' % (args.record_images_dir, v.num)
            print('Write %s' % fn)
            cv2.imwrite(fn, frame)

        #
        # Read a key.
        #

        step = False
        if args.step:
            if args.goto_num is None:
                key = cv2.waitKey(0)
                step = True
            else:
                if v.num >= args.goto_num:
                    key = cv2.waitKey(0)
                    step = True
                else:
                    key = cv2.waitKey(1)
        else:
            key = cv2.waitKey(1)

        #
        # Dispatch key.
        #

        if not dispatch_key(key, step, v):
            break


    #
    # cleanup the camera and close any open windows
    #

    v.close()
    cv2.destroyAllWindows()
    if args.record:
        print('Write %s.' % out_fn)
        vw.release()

    if args.log_fn != None:
        log_f.close()

main()
