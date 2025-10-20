import numpy as np
import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()
    width = int(cam.get(3))
    height = int(cam.get(4))
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.putText(frame, "Varol", (200, height - 10), font, 4, (120,120,120),5, cv.LINE_AA)

    cv.imshow("esff", img)

    if cv.waitKey(10) == ord("q"):
        break

cam.release()
cv.destroyAllWindows()

img = np.zeros((512,512,3),np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.line(img,(0,0),(511,511),(234,63,162),3)
cv.line(img,(0,511),(511,0),(234,63,162),3)
cv.line(img,(0,256),(511,256),(234,63,162),3)
cv.line(img,(256,0),(256,511),(234,63,162),3)
cv.rectangle(img,(0,0),(511,511),(234,63,162),5)
cv.circle(img,(256,256),20,(234,63,162),-1)
cv.putText(img,"Varol",(110,500),font,4,(234,63,162),5,cv.LINE_8)
cv.imshow("sagewg",img)
cv.waitKey(0)
cv.destroyAllWindows()