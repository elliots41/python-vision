#!/usr/bin/env python

''' differences of Gaussians .

Usage : python dog.py [<video source>]

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
    

    cv2.namedWindow("dog")
    cv2.namedWindow("gaussian1")
    cv2.namedWindow("gaussian2")
    cv2.createTrackbar('Gaussian1','dog',1,21,nothing)
    while True:

        d1=cv2.getTrackbarPos('Gaussian1','dog')
        if (d1==0):
# if the trackbar is set to 0 bang it back up to 1 as there's no such
# thing as a zero width gaussian 
           d1=1
           cv2.setTrackbarPos('Gaussian1','dog',1)
        d2=d1+2

# get an image 
        ret, frame = cap.read()
# greyscale it 
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        height,width=grey.shape
# blur it
        grey_blur1 = cv2.GaussianBlur(grey, (2*d1+1, 2*d1+1), -1)[d1:-d1,d1:-d1]
        grey_blur2 = cv2.GaussianBlur(grey, (2*d2+1, 2*d2+1), -1)[d2:-d2,d2:-d2]

#make sure they're the same size
        grey_blur2= cv2.resize(grey_blur2, (width, height)) 
        grey_blur1= cv2.resize(grey_blur1, (width, height)) 
      
#rescale
        grey_blur1=cv2.convertScaleAbs(grey_blur1);
        grey_blur2=cv2.convertScaleAbs(grey_blur2);

#actually do the Diference of Gaussians- take one blurred image away 
#from the other.
        out=grey_blur1-grey_blur2

#uncommment the next few lines and edit a bit if you want to save any of the
# images
        #fn="out/dog"+str(n).rjust(4,'0')+".png" 
        #cv2.imwrite(fn,out);
        #fn="out/gone"+str(n).rjust(4,'0')+".png" 
        #cv2.imwrite(fn,grey_blur1);
        #fn="out/gtwo"+str(n).rjust(4,'0')+".png" 
        #cv2.imwrite(fn,grey_blur2);
        #n+=1

#image show stuff
        cv2.imshow('dog', out)
        cv2.imshow('gaussian1', grey_blur1)
        cv2.imshow('gaussian2', grey_blur2)
        if cv2.waitKey(1) == 27:
            break
