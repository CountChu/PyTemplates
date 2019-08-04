import cv2
import os
import logging
import pdb
import time

class Video:

    def __init__(self):
        self.camera = None
        self.imgFnDict = None
        self.firstNum = 0               # as background.
        self.num = 0                    # current frame.
        self.beginNum = 0
        self.endNum = None        
        
    def openCamera(self):
        self.camera = cv2.VideoCapture(0)
        time.sleep(0.25)
        
    def loadVideoFile(self, videoFn):
        self.camera = cv2.VideoCapture(videoFn) 

    def loadImageFiles(self, imageDir, beginNum, endNum):
    
        #
        # Get image list
        #
        
        self.imgFnDict = {}
        for imgFn in os.listdir(imageDir):
            baseName = os.path.basename(imgFn)
            num = os.path.splitext(baseName)[0]
            num = int(num)
            imgFn = '%s/%s' % (imageDir, imgFn)
            self.imgFnDict[num] = imgFn
            
        #
        # Assign num
        #
        
        if beginNum  in self.imgFnDict:
            self.beginNum = beginNum
        else:
            self.beginNum = min(self.imgFnDict.keys())
        logging.info('beginNum = %d' % self.beginNum)    
        
        self.firstNum = min(self.imgFnDict.keys())
        logging.info('firstNum = %d' % self.firstNum)    
        
        self.num = self.firstNum
        logging.info('firstNum = %d' % self.firstNum)    
        
        #
        # Assign endNum if it is None.
        #
        
        if endNum is None:
            self.endNum = max(self.imgFnDict.keys())
        else:
            self.endNum = endNum
        
    def nextFrame(self):
        logging.info('nextFrame()')
        
        if self.camera != None:
            (grabbed, frame) = self.camera.read()
            self.num += 1
            return (grabbed, frame)
        
        if self.imgFnDict != None:
        
            '''
            if self.num >= len(self.imgFnDict) - 1:
                return (False, None)  
            '''
            
            if self.num >= self.endNum:
                return (False, None)
        
            imgFn = self.imgFnDict[self.num]
            frame = cv2.imread(imgFn)
            
            self.next()
            return (True, frame)
            
          
            
    def currentFrame(self):
    
        if self.camera != None:
            (grabbed, frame) = self.camera.read()
            return (grabbed, frame)    
    
        if self.imgFnDict != None:
            imgFn = self.imgFnDict[self.num]
            frame = cv2.imread(imgFn)
            return (True, frame)
            
    def next(self):
        logging.info('next()')
        if self.num == self.firstNum:
            if self.num != self.beginNum:
                self.num = self.beginNum
            else:
                self.num += 1
        else:
            self.num += 1    

        while True:
            if self.num not in self.imgFnDict:
                self.num += 1
            else:
                break
            if self.num > max(self.imgFnDict):
                self.num = max(self.imgFnDict)
                break

        '''
        if self.num >= len(self.imgFnDict):
            self.num = len(self.imgFnDict) - 1
        '''
        if self.endNum != None:
            if self.num > self.endNum:
                self.num -= 1
           
    def previous(self):
        self.num -= 1
        if self.num < 0:
            self.num = 0
        
    def close(self):
        if self.camera != None:
            self.camera.release()
            
def videoWriter(frame, fn):
    vw = cv2.VideoWriter(fn, getVideoType(fn), 25, (frame.shape[1], frame.shape[0]))
    return vw
            
def getVideoType(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']             

#
# Private methods.
#
    
#    
# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
#

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}       