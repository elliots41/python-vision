#!/usr/bin/env python

'''
This sample demonstrates Sobel edge detection.

Usage:
  sobel.py [<video source>]


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

# gizza window or two
    cv2.namedWindow('edge-x')
    cv2.namedWindow('edge-y')
    cv2.namedWindow('edges-all')

# gizza videocapture object
    cap = video.create_capture(fn)
    n=0;
    while True:

#read a frame from the video capture obj
        flag, img = cap.read()

#greyscale it
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sobel x  and y
        sobelx64= cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobely64= cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        both64= cv2.addWeighted(sobelx64, 0.5, sobely64, 0.5, 0)
        
        sobelx=np.uint8(np.absolute(sobelx64)) 
        sobely=np.uint8(np.absolute(sobely64)) 
        both=np.uint8(np.absolute(both64)) 
        

        cv2.imshow('edge-x',sobelx)
        cv2.imshow('edge-y',sobely)
        cv2.imshow('edges-all',both)


#open cv window management/redraw stuff 
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cv2.destroyAllWindows()
