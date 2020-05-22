import cv2
import sys 
import numpy as np

# this displays harris corners on a single image
# usage:
# python harris.py input_file.jpg

filename = sys.argv[1] if len(sys.argv)>1 else "test.jpg"
 
img = cv2.imread(filename)

#greyscale it
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# run the harris corner detector
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
fn="out/harrisfile.jpg";
cv2.imwrite(fn,img);
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
 
