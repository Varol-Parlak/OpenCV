import cv2 as cv
import numpy as np

def bos(x):
    pass
img = np.zeros((512,512,3),np.uint8)

cv.namedWindow("image")

cv.createTrackbar("R","image",0,255,bos)
cv.createTrackbar("G","image",0,255,bos)
cv.createTrackbar("B","image",0,255,bos)

while True:
    cv.imshow("image",img)
    if cv.waitKey(1) == ord("q"):
        break
    
    R = cv.getTrackbarPos("R","image")
    G = cv.getTrackbarPos("G","image")
    B = cv.getTrackbarPos("B","image")

    img[:] = [B,G,R]
cv.destroyAllWindows()