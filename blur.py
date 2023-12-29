import os
import cv2

img=cv2.imread(os.path.join(".","data","bird.jpg"))
#classical blur
k_size=100
blurred_img=cv2.blur(img,(k_size,k_size))
cv2.imshow("blur",blurred_img)
cv2.imshow("img",img)
cv2.waitKey(0)