import os
import cv2

img=cv2.imread(os.path.join(".","data","bird.jpg"))

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#the other parameter remain contant for all adaptive thresholds.
#to smooth the image
thresh=cv2.medianBlur(thresh,3)
cv2.imshow("thresh",thresh)
cv2.imshow("grayscale",img_gray)
cv2.waitKey(0)