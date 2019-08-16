# PlayImages
The Python module [plyimg](plyimg) plays images or video optionally step by step. The app is also a template. We can modify it to develop applications of computer vision.

## Usage
```
usage: -m [-h] [--verbose] [--debug] [--log LOG_FN] [--cfg] [--video VIDEO_FN]
          [--images IMAGES_DIR] [--begin BEGIN_NUM] [--end END_NUM] [--step]
          [--goto GOTO_NUM] [-r] [--ri RECORD_IMAGES_DIR] [--fps] [--bn]
          [--sd SLOWDOWN] [-t]

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

optional arguments:
  -h, --help            show this help message and exit
  --verbose             Verbose log
  --debug               Show debug messages
  --log LOG_FN          A name of a log file.
  --cfg                 Import Config.py
  --video VIDEO_FN      A path to the video file
  --images IMAGES_DIR   A directory that contains images
  --begin BEGIN_NUM     Begin of the images
  --end END_NUM         End of the images
  --step                Enable step. Press '>.' for next step and '<,' for previous step
  --goto GOTO_NUM       The argument follows --step.
  -r                    Record video.
  --ri RECORD_IMAGES_DIR
                        A directory where images are recorded
  --fps                 Display fps.
  --bn                  Display base name.
  --sd SLOWDOWN         It follows -r. It slows down the output video by specifying a number of repeated frames
  -t                    Enable transformation.
```

## CV2 Examples in [util.py](plyimg/util.py)
### def transform(frame)

The function provides examples of cv2 functions as below.
- cv2.rectangle()
- cv2.circle()
- cv2.putText()
- cv2.line()

You can try it by run the command.
```
python -m plyimg --images TestImages --step -t
```

The you can see the green and red texts and pictures drawn by Util.transform() on the below frame.

![Image](Doc/Demo1.png)
