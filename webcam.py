import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv.imshow("Başlık",frame)

    if cv.waitKey(10) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()    