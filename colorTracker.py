import cv2 
import numpy as np 

def empty(x): pass

video = cv2.VideoCapture(0)

cv2.namedWindow("trackbars")
cv2.createTrackbar("min_h","trackbars",0,179,empty)
cv2.createTrackbar("min_s","trackbars",0,255,empty)
cv2.createTrackbar("min_v","trackbars",0,255,empty)
cv2.createTrackbar("max_h","trackbars",0,179,empty)
cv2.createTrackbar("max_s","trackbars",0,255,empty)
cv2.createTrackbar("max_v","trackbars",0,255,empty)

while video.isOpened():

    ret, frame = video.read()
    frame = cv2.flip(frame,1)
    if not ret:
        break

    min_h = cv2.getTrackbarPos("min_h", "trackbars")
    min_s = cv2.getTrackbarPos("min_s", "trackbars")
    min_v = cv2.getTrackbarPos("min_v", "trackbars")
    max_h = cv2.getTrackbarPos("max_h", "trackbars")
    max_s = cv2.getTrackbarPos("max_s", "trackbars")
    max_v = cv2.getTrackbarPos("max_v", "trackbars")
    min_np = np.array([min_h, min_s, min_v])
    max_np = np.array([max_h, max_s, max_v])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, min_np, max_np)

    kernel = np.ones((5,5), np.uint8)
    eroded = cv2.erode(mask, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    biggest = None
    if contours:
        # track = 0
        # biggest = None
        # for contour in contours:
        #     area = cv2.contourArea(contour)
        #     if area > track:
        #         track = area
        #         biggest = contour
        biggest = max(contours, key = cv2.contourArea)

    x, y, w, h = cv2.boundingRect(biggest)

    cv2.rectangle(frame, (x,y), (x + w, y + h), (48,240,24), 2, cv2.LINE_AA)

    cv2.imshow("masked_eroded_dilated",dilated)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
video.release()