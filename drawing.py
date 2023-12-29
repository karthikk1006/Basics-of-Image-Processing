import os
import cv2

img=cv2.imread(os.path.join(".","data","whiteboard.jpg"))
print(img.shape)
#line
cv2.line(img,(100,100),(300,200),(0,0,255),2)


#rectange
#upperleft and bottom right crner as coordinates
cv2.rectangle(img,(90,100),(400,300),(255,0,0),3)

#circle
cv2.circle(img,(150,250),100,(0,255,0),4)

#text

cv2.putText(img,"hello there",(200,300),6,2.0,(0,0,255),6)




cv2.imshow("whiteboard",img)
cv2.waitKey(0)