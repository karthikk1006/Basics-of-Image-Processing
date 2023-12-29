import os
import cv2

img=cv2.imread(os.path.join(".","data","bird.jpg"))


img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


img_bw=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("bw",img_bw)
cv2.imshow("rgb",img_rgb)
cv2.imshow("bird",img)
cv2.waitKey(0)