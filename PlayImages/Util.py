#
# FILENAME.
#       Util.py - Utility Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module provide app with API.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/8/11
#

#
# Include standard packages.
#

import pdb
import cv2

#
# Include specific packages.
#

#
# It handles them.
#

def transform(frame):

    #
    # Define colors
    #

    green = (0, 255, 0)                 # green
    red = (0, 0, 255)                   # red
    white = (255, 255, 255)             # white

    #
    # Define the layout.
    #

    x0 = 200
    y0 = 300
    dx = 20
    dy = 20

    #
    # Draw rectangles
    #

    x = x0
    y = y0
    w = 30
    h = 40
    cv2.rectangle(frame, (x, y, w, h), green)

    y += h + 10
    cv2.rectangle(frame, (x, y, w, h), green, cv2.FILLED)

    #
    # Draw circles
    #

    x += (w+20)
    y = y0
    cv2.circle(frame, (x, y), 2, red, -1)

    y += dy
    cv2.circle(frame, (x, y), 4, red, -1)

    y += dy
    cv2.circle(frame, (x, y), 6, red, -1)

    y += dy
    cv2.circle(frame, (x, y), 2, red, 1)

    y += dy
    cv2.circle(frame, (x, y), 4, red, 1)

    y += dy
    cv2.circle(frame, (x, y), 6, red, 1)

    y += dy
    cv2.circle(frame, (x, y), 2, red, 2)

    y += dy
    cv2.circle(frame, (x, y), 4, red, 2)

    y += dy
    cv2.circle(frame, (x, y), 6, red, 2)

    #
    # Draw texts
    #

    x += dx
    y = y0
    cv2.putText(frame, "Test", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.4, green)

    y += dy
    cv2.putText(frame, "Test it.", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, green)

    y += dy
    cv2.putText(frame, "Test it.", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, green)

    y += dy
    cv2.putText(frame, "Test it.", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, green)

    y += dy
    cv2.putText(frame, "Test it.", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, green, 2)

    y += dy
    cv2.putText(frame, "Test it.", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, green, 2)

    y += dy
    cv2.putText(frame, "Test it.", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, green, 2)

    #
    # Draw lines
    #

    x += 80

    y = y0
    cv2.line(frame, (x, y), (x+40, y+10), red, 1)

    y += dy
    cv2.line(frame, (x, y), (x+40, y+10), red, 2)

    y += dy
    cv2.line(frame, (x, y), (x+40, y+10), red, 1, cv2.LINE_AA)

    y += dy
    cv2.line(frame, (x, y), (x+40, y+10), red, 2, cv2.LINE_AA)
