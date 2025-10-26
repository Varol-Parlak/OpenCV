import cv2  
import numpy as np 

def empty(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("window")

t1_trackbar = cv2.createTrackbar("lower_threshold", "window", 155, 255, empty)
t2_trackbar = cv2.createTrackbar("upper_threshold", "window", 130, 255, empty)

while cap.isOpened():
    _, frame = cap.read()
    flipped = cv2.flip(frame, 1)
    t1_value = cv2.getTrackbarPos("lower_threshold", "window")
    t2_value = cv2.getTrackbarPos("upper_threshold", "window")

    gray = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, t1_value, t2_value)
    cv2.imshow("window", canny)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()