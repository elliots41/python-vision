import cv2
import video
import common
import sys
import numpy as np


def nothing(*arg):
   pass

cv2.namedWindow('cameraview')
cv2.createTrackbar('value','cameraview',20,255,nothing)

cam = video.create_capture(0)

while True:
   # read an image from the video camera
   ret, img = cam.read()

   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
   brightness=cv2.getTrackbarPos('value','cameraview')
   h, s, v = cv2.split(hsv)
   v=cv2.add(brightness,v) 
   # we do this instead of  v += 30 because cv2.add() will not go over 255
   final_hsv = cv2.merge((h, s, v))

   img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
  
   # put that image in the window 
   cv2.imshow('cameraview', img)

   # listen for a key (waitKey also redraws image, so is pretty
   # important. if the key is 27, quit 
   if 0xFF & cv2.waitKey(5) == 27:
      break


