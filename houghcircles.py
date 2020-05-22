#!/usr/bin/env python

'''
This sample demonstrates hough circle detection.
It'll open the webcam (if there is one) and draw circles
If you want to save out frames to make a video, uncomment the 
bit below on output 
'''

import math
import numpy as np
import cv2
import video
import sys


if __name__ == '__main__':
    print __doc__


    # if there's an argument use that as an input stream name or
    # a video file
    try: fn = sys.argv[1]
    except: fn = 0

    def nothing(*arg):
        pass

    # create an output window 
    cv2.namedWindow('hough')
    cv2.createTrackbar('canny1','hough',30,100,nothing)
    cv2.createTrackbar('canny2','hough',20,100,nothing)
    cv2.createTrackbar('minimum radius','hough',30,100,nothing)
    cv2.createTrackbar('maximum radius','hough',50,100,nothing)

    # open the input video stream
    cap = video.create_capture(fn)
    n=0;
    while True:
        # read an image from the stream
        flag,img = cap.read()
        # greyscale it 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # blur it 
        blur = cv2.medianBlur(gray,5) 
        # copy it 
        houghcircle_visualisation=img.copy()
        # get the params from the trackbars
        c1=cv2.getTrackbarPos('canny1','hough')
        c2=cv2.getTrackbarPos('canny2','hough')
        minr=cv2.getTrackbarPos('minimum radius','hough')
        maxr=cv2.getTrackbarPos('maximum radius','hough')
        # opencv magic function which triggers all the drawing stuff 
        ch = cv2.waitKey(5)
         
        # actually do the hough
	circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10,param1=c1,param2=c2,minRadius=minr,maxRadius=maxr)
        
        # draw some stuff
        if circles is not None:
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
		    cv2.circle(houghcircle_visualisation, (i[0], i[1]), i[2], (0, 0, 255), 3)
		    cv2.circle(houghcircle_visualisation, (i[0], i[1]), i[2], (0, 255, 0), 3) # draw center of circle


        # bung the visualisation in the window
        cv2.imshow('hough', houghcircle_visualisation)


     #  if you'd like to save out the files uncomment the next 3 lines
     #  and create a directory called "out" 
     #   fn="out/houghcircle"+str(n).rjust(4,'0')+".png" 
     #   cv2.imwrite(fn,houghcircle_visualisation);
     #   n+=1

     # deal with quitting the window and so on
        if ch == 27:
            break
    cv2.destroyAllWindows()
