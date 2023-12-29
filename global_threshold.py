import os
import cv2

img=cv2.imread(os.path.join(".","data","bird.jpg"))

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


ret,thresh=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
#80 is global threshold,all values below 80 will be taken to 0 and all values above 80 will be taken to 1 or 255


cv2.imshow("thresh",thresh)
cv2.imshow("grayscale",img_gray)
cv2.waitKey(0)