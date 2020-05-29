import cv2
import sys 
import numpy as np


# this displays surf detections on a single image
# usage:
# python surf.py input_file.jpg

filename = sys.argv[1] if len(sys.argv)>1 else "test.jpg"



img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Create SURF object. You can specify params here or later.
# The main parameter is the Hessian threshold - this is to do with 
# the curvature (the chance of a point being counted as a feature)

surf = cv2.SURF(500)

# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)

img=cv2.drawKeypoints(gray,kp,img,[0,255,255])

cv2.imwrite('surf_keypoints.jpg',img)
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
 
