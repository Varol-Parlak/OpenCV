import cv2 as cv
import numpy as np

def cagir(event,x,y,flags,param):

    if event == cv.EVENT_MOUSEMOVE:
        cv.circle(img,(x,y),20,(244,151,64),-1)
       

img = cv.imread("E:\Python\OpenCV\Photos\dog.jpg")
cv.namedWindow("image")
cv.setMouseCallback("image",cagir)
while(1):
    cv.imshow("image",img)
    if cv.waitKey(20) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()

def bos(x):
    pass
bas = False
def ciz(event,x,y,flags,param):  
    global bas
    
    if event == cv.EVENT_LBUTTONDOWN:
        bas = True
    if event == cv.EVENT_MOUSEMOVE:
        if bas == True:
            cv.circle(img, (x,y),20,(G,B,R),-1)
        else:
            pass
    if event == cv.EVENT_LBUTTONUP:
        bas = False

img = cv.imread("E:\Python\OpenCV\Photos\dog.jpg")
cv.namedWindow("image")

cv.createTrackbar("R","image",0,255,bos)
cv.createTrackbar("B","image",0,255,bos)
cv.createTrackbar("G","image",0,255,bos)

while(1):
    
    R = cv.getTrackbarPos("R","image")
    G = cv.getTrackbarPos("B","image")
    B = cv.getTrackbarPos("G","image")
    cv.setMouseCallback("image",ciz)
    cv.imshow("image",img)
    key = cv.waitKey(1)
    if key == ord("q"):
        break

