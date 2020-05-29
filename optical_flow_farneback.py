import cv2
import numpy as np
import video
import sys


n=0
try: infn = sys.argv[1]
except: infn = 0

cap = video.create_capture(infn)

print "opening"
print infn

ret, frame1 = cap.read()
tmp= cv2.resize(frame1, (0,0), fx=0.5, fy=0.5) 
prvs= cv2.cvtColor(tmp,cv2.COLOR_BGR2GRAY) #prvs = 1 channel, small
hsv = np.zeros_like(tmp)
hsv[...,1] = 255
#params of the farneback optical flow (it's multiscale):
#cv2.calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags)

while(1):
    print n
    ret, frame2 = cap.read()
    tmp = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
#resize or it'll take aeons
    nxt= cv2.resize(tmp, (0,0), fx=0.5, fy=0.5) 
# just use the standard params
    flow = cv2.calcOpticalFlowFarneback(prvs, nxt, None, 0.5, 3, 15, 3, 5, 1.2, 0)

#do the visualisation
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    cv2.imshow('frame2',rgb)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
#output lines, uncomment if you wanna save
    #fn="out/denseoptflowcr_moving"+str(n).rjust(4,'0')+".png" 
    #cv2.imwrite(fn,rgb);
    n=n+1


    prvs = nxt

cap.release()
cv2.destroyAllWindows()
