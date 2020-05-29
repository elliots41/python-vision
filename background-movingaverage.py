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
    cv2.namedWindow('input')
    cv2.createTrackbar('Size of buffer', 'bgmodel', 110, 500, nothing)
    cv2.createTrackbar('Difference threshold', 'bgmodel', 10, 200, nothing)

    n=0
# gizza videocapture object
    cap = video.create_capture(fn)

    flag, img = cap.read()
    movingaverage=np.float32(img)
    while True:

#read a frame from the video capture obj

        flag, img = cap.read()
           

        fbuffer=cv2.getTrackbarPos('Size of buffer', 'bgmodel')
#let's deal with that pesky zero case before we divide by fbuffer
        if fbuffer==0:
            fbuffer=1
        alpha=float(1.0/fbuffer) 
        cv2.accumulateWeighted(img,movingaverage,alpha) 

# do the drawing stuff
        res=cv2.convertScaleAbs(movingaverage)
# show the background model 
        cv2.imshow('bgmodel', res)

#resize the input just so i can have a smaller window and still show the input
#on a little laptop screen
        tmp= cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        cv2.imshow('input', tmp)

# take the absolute difference of the background and the input
        difference_img = cv2.absdiff(res, img)
# make that greyscale

        grey_difference_img = cv2.cvtColor(difference_img, cv2.COLOR_BGR2GRAY)
# threshold it to get a motion mask 
        difference_thresh=cv2.getTrackbarPos('Difference threshold', 'bgmodel')
        ret,th1 = cv2.threshold(grey_difference_img,difference_thresh,255,cv2.THRESH_BINARY)
        cv2.imshow('foregound',th1)

#uncommment the next few lines if you want to save the output
        #fn="out/bgmovingav_big"+str(n).rjust(4,'0')+".png" 
        #cv2.imwrite(fn,th1);
        #fn="out/bgmovingav_bg_big"+str(n).rjust(4,'0')+".png" 
        #cv2.imwrite(fn,res);
        n+=1
 

#open cv window management/redraw stuff 
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cv2.destroyAllWindows()
