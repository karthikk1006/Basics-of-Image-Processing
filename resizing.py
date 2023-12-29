import os
import cv2

img=cv2.imread(os.path.join(".","data","bird.jpg"))

resized_img=cv2.resize(img,(700,500))


print(resized_img.shape)
cv2.imshow("bird",resized_img)
cv2.waitKey(0)