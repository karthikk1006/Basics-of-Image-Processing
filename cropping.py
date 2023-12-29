import os
import cv2

img1=cv2.imread(os.path.join(".","data","mountain.jpg"))
img=cv2.resize(img1,(1000,400))

cropped_img=img[200:300,200:600]


cv2.imshow("mountain",img)
cv2.imshow("crop",cropped_img)
cv2.waitKey(0)

