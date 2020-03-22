#
# FILENAME.
#       Video.py - Video Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module privides API to open cam, play a video, and play images.
#
# NOTICE.
#       COMPANY_NAME Confidential
#       COPYRIGHT COMPANY_NAME 2019 All RIGHTS RESERVED
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/4/24
#

#
# Include standard packages.
#

import cv2
import os
import logging
import pdb
import time

#
# Include specific packages.
#

#
#   The class provides features as below to play images or video.
#   1. open a cam
#   2. load a video file
#   3. load images.
#   4. play the next image (or frame)
#   5. play the previous image (or frame)
#

class Video:

    GLOBAL_DEVICE_LIST = {}

    VIDEO_SUPPORT_FORMAT = ['.mp4', '.avi']

    def __init__(self):
        self.cam = None
        self.img_fn_dict = None
        self.first_num = 0              # as background.
        self.num = 0                    # current frame.
        self.begin_num = 0
        self.end_num = None
        self.device = None

    def open_cam(self, device=0):
        if device in Video.GLOBAL_DEVICE_LIST.keys():
            logging.error('Error. device %d already used' % device)
            return False

        #
        # Maybe allocate a previous video instance during GLOBAL_DEVICE_LIST
        #

        Video.GLOBAL_DEVICE_LIST[device] = (self, 1)
        self.device = device
        self.cam = cv2.VideoCapture(device)
        time.sleep(0.25)

        return True

    def load_video_file(self, video_fn):
        if not os.path.exists(video_fn) or video_fn.split('.')[-1] not in self.VIDEO_SUPPORT_FORMAT:
            logging.info('Error. Check the video path %s' % (video_fn))
        self.cam = cv2.VideoCapture(video_fn)

    def load_image_files(self, image_dir, begin_num, end_num):

        #
        # Get bnList of base name list.
        #

        id_list = []
        for img_fn in os.listdir(image_dir):
            bn = os.path.basename(img_fn)
            id = os.path.splitext(bn)[0]
            id_list.append(id)

        is_digit = True
        for id in id_list:
            if not id.isdigit():
                is_digit = False
                break

        is_digit_str = True
        if is_digit:
            length = len(id_list[0])
            for id in id_list:
                if length != len(id):
                    is_digit_str = False


        newid_list = []
        for id in id_list:
            if is_digit and not is_digit_str:
                id = int(id)
                newid_list.append(id)
            else:
                newid_list.append(id)
        newid_list.sort()

        id_dict = {}
        for i, id in enumerate(newid_list):
            if is_digit:
                id_dict[str(id)] = i
            else:
                id_dict[id] = i
        #pdb.set_trace()

        #
        # Get image list
        #

        self.img_fn_dict = {}
        for img_fn in os.listdir(image_dir):
            bn = os.path.basename(img_fn)
            id = os.path.splitext(bn)[0]
            num = id_dict[id]
            img_fn = '%s/%s' % (image_dir, img_fn)
            self.img_fn_dict[num] = img_fn
        #pdb.set_trace()

        #
        # Assign num
        #

        if begin_num  in self.img_fn_dict:
            self.begin_num = begin_num
        else:
            self.begin_num = min(self.img_fn_dict.keys())
        logging.info('begin_num = %d' % self.begin_num)

        self.first_num = min(self.img_fn_dict.keys())
        logging.info('first_num = %d' % self.first_num)

        self.num = self.first_num
        logging.info('first_num = %d' % self.first_num)

        #
        # Assign end_num if it is None.
        #

        if end_num is None:
            self.end_num = max(self.img_fn_dict.keys())
        else:
            self.end_num = end_num

    def next_frame(self):
        logging.info('next_frame()')

        if self.cam != None:
            (grabbed, frame) = self.cam.read()
            self.num += 1
            return (grabbed, frame)

        if self.img_fn_dict != None:

            '''
            if self.num >= len(self.img_fn_dict) - 1:
                return (False, None)
            '''

            if self.num >= self.end_num:
                return (False, None)

            img_fn = self.img_fn_dict[self.num]
            frame = cv2.imread(img_fn)

            self.next()
            return (True, frame)

    def cur_frame(self):

        if self.cam != None:
            (grabbed, frame) = self.cam.read()
            return (grabbed, frame)

        if self.img_fn_dict != None:
            img_fn = self.img_fn_dict[self.num]
            frame = cv2.imread(img_fn)
            return (True, frame)

    def next(self):
        logging.info('next()')
        if self.num == self.first_num:
            if self.num != self.begin_num:
                self.num = self.begin_num
            else:
                self.num += 1
        else:
            self.num += 1

        while True:
            if self.num not in self.img_fn_dict:
                self.num += 1
            else:
                break
            if self.num > max(self.img_fn_dict):
                self.num = max(self.img_fn_dict)
                break

        '''
        if self.num >= len(self.img_fn_dict):
            self.num = len(self.img_fn_dict) - 1
        '''
        if self.end_num != None:
            if self.num > self.end_num:
                self.num -= 1

    def previous(self):
        self.num -= 1
        if self.num < 0:
            self.num = 0

    def close(self):
        if self.cam != None:
            self.cam.release()

        #
        # Del the last reference device
        #
        
        if self.device != None:
            if Video.GLOBAL_DEVICE_LIST[self.device][1] == 1:
                del Video.GLOBAL_DEVICE_LIST[self.device]
            else:
                Video.GLOBAL_DEVICE_LIST[self.device][1] -= 1
            print('Close cam %d' % self.device)

def video_writer(frame, fn):
    vw = cv2.VideoWriter(fn, get_video_type(fn), 25, (frame.shape[1], frame.shape[0]))
    return vw

def get_video_type(fn):
    (_, ext) = os.path.splitext(fn)
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
    'mp4': cv2.VideoWriter_fourcc('M','J','P','G'),
}

if __name__ == '__main__':
    custom_video1 = Video()
    if custom_video1.open_cam(device=0):
        print('first open')


    custom_video2 = Video()
    if custom_video2.open_cam(device=0):
        print('reopen')
        custom_video2.close()

    custom_video1.close()
    print('end')
