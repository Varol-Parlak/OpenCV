import cv2
import numpy as np

kernel = np.ones((3,3), np.uint8)
img = cv2.imread("doc.jpg")
img = cv2.resize(img, (1000,550))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (11,11), 0)

canny = cv2.Canny(blur, 50, 150)
dilated = cv2.dilate(canny, kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse=False)
doc = None
for con in contours[:5]:
    perimeter = cv2.arcLength(con, True)
    approx = cv2.approxPolyDP(con, 0.02 * perimeter, True)

    area = cv2.contourArea(con)
    if len(approx) == 4:
        doc = approx
        break

if doc is not None:
    cv2.drawContours(img, [doc], -1, (0, 255, 0), 2)
else: 
    print("Couldnt find the document.")

cv2.imshow("ret", img)
cv2.imshow("fw", dilated)

cv2.waitKey(0)