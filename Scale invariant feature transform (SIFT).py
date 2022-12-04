import numpy as np
import cv2 


img = cv2.imread('img2.jpg')
cv2.imshow('Original Image', img)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)




sift = cv2.SIFT_create()
kp = sift.detect(gray,None)
img=cv2.drawKeypoints(gray,kp,img)

#img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow('sift_keypoints',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

