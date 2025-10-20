import cv2
import random

img_normal = cv2.imread("E:\Python\OpenCV\Photos\dog.jpg")
img_resize = cv2.imread("E:\Python\OpenCV\Photos\dog.jpg")

img_resize = cv2.resize(img_resize,(0,0),fx=0.5 , fy=0.5)
img_resize = cv2.rotate(img_resize, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("OpenCV/Photos/rotated.jpg",img_resize)

cv2.imshow("Dog_resize",img_resize)
cv2.imshow("Dog_normal",img_normal)
cv2.waitKey(0)
