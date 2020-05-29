import cv2
import sys 
import numpy as np


# this displays orb detections on a single image
# usage:
# python orb.py input_file.jpg


filename = sys.argv[1] if len(sys.argv)>1 else "test.jpg"

img = cv2.imread(filename)
greyimg= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

detector = cv2.FeatureDetector_create("ORB")
descriptorExtractor = cv2.DescriptorExtractor_create("ORB")
keypoints = detector.detect(greyimg)
(keypoints, descriptors) = descriptorExtractor.compute(greyimg, keypoints)



img=cv2.drawKeypoints(greyimg,keypoints,img)

cv2.imwrite('orb_keypoints.jpg',img)
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
 
