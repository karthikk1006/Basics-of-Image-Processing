import os
import cv2

img=cv2.imread(os.path.join(".","data","bird.jpg"))


img_edge=cv2.Canny(img,100,200)

cv2.imshow("img",img)
cv2.imshow("image_edge",img_edge)
cv2.waitKey(0)