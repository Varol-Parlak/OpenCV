import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

write = ""

top = 100
bottom = 300
left = 100
right = 500
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    
    cv2.rectangle(frame, (left,top), (right,bottom), (0,255,0), 2, cv2.LINE_AA)
    search_frame = frame[top:bottom, left:right]

    key = cv2.waitKey(1)
    if key == ord("s"):
        gray = cv2.cvtColor(search_frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY_INV, 17, 5)
        text = pytesseract.image_to_string(thresh)
        write = text
    
    if write:
        cv2.putText(frame, text, (30,50), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)

    cv2.imshow("frame", frame)
    
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()