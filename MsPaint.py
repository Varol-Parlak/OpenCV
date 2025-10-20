import cv2 as cv
import numpy as np

def bos(x):
    pass

img = cv.imread("E:\Python\OpenCV\Photos\orman.jpg")
matrix2 = None
img_copy = img.copy()
mod = 0
size = 15
drawing = False


def ciz(event,x,y,flags,param):
    global matrix2, mod, color, drawing
    color = (B,G,R)

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv.EVENT_MOUSEMOVE:
        if mod == 0 and drawing == True:
            cv.rectangle(img,(x-size, y+size),(x+size, y-size),color,-1)

        elif mod == 1 and drawing == True:
            matrix2 = img_copy[min(y+size,y-size):max(y+size,y-size), min(x+size,x-size):max(x+size,x-size)]
            img[min(y+size,y-size):max(y+size,y-size), min(x+size,x-size):max(x+size,x-size)] = matrix2

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        
    cv.imshow("image", img)
        
cv.imshow("image", img)

cv.createTrackbar("R","image",0,255,bos)
cv.createTrackbar("B","image",0,255,bos)
cv.createTrackbar("G","image",0,255,bos)


while 1 :

    R = cv.getTrackbarPos("R","image")
    G = cv.getTrackbarPos("B","image")
    B = cv.getTrackbarPos("G","image")
    cv.setMouseCallback("image",ciz)

    key = cv.waitKey(1)
    if key == ord("q"):
        break

    elif key == ord("e"):
        mod = 1

    elif key == ord("d"):
        mod = 0

    cv.imshow("image",img)
    
cv.destroyAllWindows()


