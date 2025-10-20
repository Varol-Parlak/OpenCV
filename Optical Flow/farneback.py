import cv2
import numpy as np
import time 

def bounding_box(img, flow, limit):
    h, w = img.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]

    buyukluk = np.sqrt(fx**2 + fy**2)
    movement_mask = (buyukluk > limit).astype(np.uint8)
    x, y, width, height = cv2.boundingRect(movement_mask)
    cv2.rectangle(img, (x, y), (x + width, y + height), (123, 23, 156), 2)

    return img

def ciz2(img, flow, step=8):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T

    lines = np.vstack([x, y, x-fx, y-fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)

    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(img_bgr, lines, 0, (0, 255, 0))

    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)

    return img_bgr

cap = cv2.VideoCapture("cutted.avi")


_, prev = cap.read()
prev = cv2.resize(prev, (640,480))
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

while True:
    _, img = cap.read()
    img = cv2.resize(img, (640,480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    start = time.time()
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    prevgray = gray
    end = time.time()
    fps = 1/(end-start)
    print(int(fps))
    cv2.imshow('wef', bounding_box(ciz2(gray, flow), flow, limit=1.0))

    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
