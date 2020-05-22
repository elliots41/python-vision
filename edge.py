#!/usr/bin/env python

'''
This sample demonstrates Canny edge detection.

Usage:
  edge.py [<video source>]

  Trackbars control edge thresholds.

'''

import cv2
import video
import sys


if __name__ == '__main__':
    print __doc__

# if we have a filename let's have a go at opening that...
    try: fn = sys.argv[1]
    except: fn = 0

    def nothing(*arg):
        pass

# gizza window
    cv2.namedWindow('edge')
# gizza couple of UI elements to fiddle with the parameters
    cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)

# gizza videocapture object
    cap = video.create_capture(fn)
    n=0;
    while True:

#read a frame from the video capture obj
        flag, img = cap.read()

#greyscale it
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#get parameters from the trackbars
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
# actually run the canny
        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)

# do the drawing stuff
        vis = img.copy()
        vis /= 2
        vis[edge != 0] = (0, 255, 0)
        cv2.imshow('edge', vis)

#uncommment the next three lines if you want to save the output
   #     n=n+1;
   #     fn="out/edgefile"+str(n).rjust(4,'0')+".png" 
  #      cv2.imwrite(fn,vis);
 

#open cv window management/redraw stuff 
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cv2.destroyAllWindows()
