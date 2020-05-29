import numpy as np
import cv2
import video

try: infn = sys.argv[1]
except: infn = 0

cv2.namedWindow('foreground')
 
cap = video.create_capture(infn)

fgbg = cv2.BackgroundSubtractorMOG()
fn=0 
while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    cv2.imshow('foreground',fgmask)
    cv2.imshow('input',frame)
    k = cv2.waitKey(5) 
    print "In frame {}".format(fn)
    fn+=1
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
