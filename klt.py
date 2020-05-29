import numpy as np
import cv2
import sys

filename = sys.argv[1] if len(sys.argv)>1 else "test.jpg"


img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)




for i in corners:
    x,y = i.ravel() # a numpy array reshaping thingy
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('dst',img)

fn="out/kltfile.jpg";
cv2.imwrite(fn,img);
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
 
