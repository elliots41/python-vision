#!/usr/bin/env python

'''
This sample demonstrates simple background detection.

Usage:
  background-simple.py [<video source>]

  Trackbar controls average buffer size 

'''

import cv2
import video
import sys
import numpy as np


if __name__ == '__main__':
    print __doc__

# if we have a filename let's have a go at opening that...
    try: fn = sys.argv[1]
    except: fn = 0

    def nothing(*arg):
        pass

# gizza window with a trackbar on it
    cv2.namedWindow('bgmodel')
    cv2.namedWindow('foregound')
    cv2.createTrackbar('Difference threshold', 'bgmodel', 10, 200, nothing)

    n=0
# gizza videocapture object
    cap = video.create_capture(fn)

    flag, bgimg = cap.read()
    while True:

#read a frame from the video capture obj

        flag, img = cap.read()
           


# show the background model 
        cv2.imshow('bgmodel', bgimg)

# take the absolute difference of the background and the input
        difference_img = cv2.absdiff(bgimg, img)
# make that greyscale

        grey_difference_img = cv2.cvtColor(difference_img, cv2.COLOR_BGR2GRAY)
# threshold it to get a motion mask 
        difference_thresh=cv2.getTrackbarPos('Difference threshold', 'bgmodel')
        ret,th1 = cv2.threshold(grey_difference_img,difference_thresh,255,cv2.THRESH_BINARY)
        cv2.imshow('foregound',th1)

#uncommment the next three lines if you want to save the output
        fn="out/bgsimple_smallthresh"+str(n).rjust(4,'0')+".png" 
        cv2.imwrite(fn,th1);
        fn="out/bgsimple_bgmod_smallthresh"+str(n).rjust(4,'0')+".png" 
        cv2.imwrite(fn,bgimg);
        n+=1
 

#open cv window management/redraw stuff 
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cv2.destroyAllWindows()
