import cv2
import numpy as np

backSub = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((3,3), np.uint8)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret , frame = cap.read()
    if not ret:
        print("hata")
        break
    
    frame = cv2.flip(frame, 1)
    
    fgMask = backSub.apply(frame)
    dilated = cv2.dilate(fgMask, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 12000:
            continue
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

cap.release()
