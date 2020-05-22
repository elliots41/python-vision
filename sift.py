import cv2
import sys 
import numpy as np


# this displays sift detections on a single image
# usage:
# python sift.py input_file.jpg


filename = sys.argv[1] if len(sys.argv)>1 else "test.jpg"


img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


sift = cv2.SIFT()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp,img,[255,255,0])

cv2.imwrite('sift_keypoints.jpg',img)
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
 
