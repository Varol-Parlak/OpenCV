import cv2 
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
line_thickness = 3
while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) it got worse with thresholding for some reason

        detected = decode(gray)

        for i in detected:
            if i.data.decode("utf-8") == "Varol Parlak":
                p1_x, p2_x, p3_x, p4_x = i.polygon[0][0], i.polygon[1][0], i.polygon[2][0], i.polygon[3][0]
                p1_y, p2_y, p3_y, p4_y = i.polygon[0][1], i.polygon[1][1], i.polygon[2][1], i.polygon[3][1]

                cv2.line(frame, (p1_x, p1_y), (p2_x, p2_y), (0, 0, 0), line_thickness)
                cv2.line(frame, (p2_x, p2_y), (p3_x, p3_y), (0, 0, 0), line_thickness)
                cv2.line(frame, (p3_x, p3_y), (p4_x, p4_y), (0, 0, 0), line_thickness)
                cv2.line(frame, (p4_x, p4_y), (p1_x, p1_y), (0, 0, 0), line_thickness)

        cv2.imshow("window", frame)
        if cv2.waitKey(1) == ord("q"):
            break

cv2.destroyAllWindows()
cap.release()