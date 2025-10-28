import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((5,5), np.uint8)
while cap.isOpened():
    _, frame1 = cap.read()
    _, frame2 = cap.read()
    frame1 = cv2.flip(frame1, 1)
    frame2 = cv2.flip(frame2, 1)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray2, gray1)

    _, thres_frame = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
    blur_mask = cv2.GaussianBlur(thres_frame, (21, 21), 0)
    dilated = cv2.dilate(blur_mask, kernel, iterations=4)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        
        if cv2.contourArea(contour) < 2000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0,255,0), 2)
        else:
            continue
    
    cv2.imshow("sgsw", frame1)
    
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
