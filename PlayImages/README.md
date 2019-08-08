# PlayImages
The Python PlayImages.py plays images or video optionally step by step. The app is also a template. We can modify it to develop applications of computer vision.

## Usage
```
Usage: PlayImages.py [-h] [-v] [--video VIDEOFN] [--images IMAGESDIR]
                     [--begin BEGINNUM] [--end ENDNUM] [--step]
                     [--goto GOTONUM] [-r] [--log LOGFN]
                     [--ri RECORDIMAGESDIR] [--fps] [--bn] [--sd SLOWDOWN]

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

optional arguments:
  -h, --help            show this help message and exit
  -v                    Verbose log
  --video VIDEOFN       A path to the video file
  --images IMAGESDIR    A directory that contains images
  --begin BEGINNUM      Begin of the images
  --end ENDNUM          End of the images
  --step                Enable step. Press '>.' for next step and '<,' for previous step
  --goto GOTONUM        The argument follows --step.
  -r                    Record video.
  --log LOGFN           A name of a log file.
  --ri RECORDIMAGESDIR  A directory where images are recorded
  --fps                 Display fps.
  --bn                  Display base name.
  --sd SLOWDOWN         It follows -r. It slows down the output video by specifying a number of repeated frames
```