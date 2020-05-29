#!/usr/bin/env python

''' Laplacian blurs .

Usage : python laplacian.py [<video source>]

'''

import numpy as np
import cv2
import video
from common import nothing, getsize

n=0;

if __name__ == '__main__':
    import sys
    print __doc__

    try:
        fn = sys.argv[1]
    except:
        fn = 0
    cap = video.create_capture(fn)

    while True:
        ret, frame = cap.read()
        d=5	
# blur it
        img_blur = cv2.GaussianBlur(frame, (2*d+1, 2*d+1), -1)[d:-d,d:-d]
# greyscale it 
        grey_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY) 
# do the laplacian
        laplacian1 = cv2.Laplacian(grey_blur, cv2.CV_16S, 11, 5, 2, cv2.BORDER_DEFAULT)
# do the sobel x and the sobel y and the sobel both
	sobelx = cv2.Sobel(grey_blur,cv2.CV_64F,1,0,ksize=5)
	sobely = cv2.Sobel(grey_blur,cv2.CV_64F,0,1,ksize=5)
	sobelboth = cv2.Sobel(grey_blur,cv2.CV_64F,1,1,ksize=5)

#rescale 
        laplacian1=cv2.convertScaleAbs(laplacian1)
        sobelx=cv2.convertScaleAbs(sobelx)
        sobely=cv2.convertScaleAbs(sobely)
        sobelboth=cv2.convertScaleAbs(sobelboth)


#uncommment the next 3 lines and edit output1 if you want to save any of the
# images
#        fn="out/l1"+str(n).rjust(4,'0')+".png" 
#        cv2.imwrite(fn,laplacian1);
#        n+=1

#image show stuff
        cv2.imshow('laplacian ', laplacian1)
        cv2.imshow('sobelx', sobelx)
        cv2.imshow('sobely', sobely)
        cv2.imshow('sobel', sobelboth)
        if cv2.waitKey(1) == 27:
            break
