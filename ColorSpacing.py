import cv2 as cv
import numpy as np
def nothing(x):
    pass
cap = cv.VideoCapture(0)

cv.namedWindow("frame")

cv.createTrackbar("H1","frame",0,359,nothing)
cv.createTrackbar("H2","frame",0,359,nothing)
cv.createTrackbar("S1","frame",0,255,nothing)
cv.createTrackbar("S2","frame",0,255,nothing)
cv.createTrackbar("V1","frame",0,255,nothing)
cv.createTrackbar("V2","frame",0,255,nothing)



while cap.isOpened():
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    H1 = int(cv.getTrackbarPos("H1","frame")/2)
    H2 = int(cv.getTrackbarPos("H2","frame")/2)
    S1 = cv.getTrackbarPos("S1","frame")
    S2 = cv.getTrackbarPos("S2","frame")
    V1 = cv.getTrackbarPos("V1","frame")
    V2 = cv.getTrackbarPos("V2","frame")

    lower = np.array([H1,S1,V1])
    upper = np.array([H2,S2,V2])

    mask = cv.inRange(hsv,lower,upper)

    res = cv.bitwise_and(frame,frame,mask=mask)
    
    cv.imshow("frame",mask)
    cv.imshow("fram",frame)
        
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()