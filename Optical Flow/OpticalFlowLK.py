import cv2 as cv
import numpy as np

ix ,iy,k = 123,123,1
def onMouse(event,x,y,flags,params):
    global ix ,iy,k
    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        k = -1

cv.namedWindow("ekran")
cv.setMouseCallback("ekran", onMouse)

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv.imshow("ekran",frame)

    if cv.waitKey(1) == 27 or k == -1:
        old_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.destroyAllWindows()
        break

old_pts = np.array([[ix, iy]], dtype="float32").reshape(-1,1,2)
mask = np.zeros_like(frame) 

while True:
    _, frame2 = cap.read()
    new_gray = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)

    new_pts,status,err = cv.calcOpticalFlowPyrLK(old_gray,new_gray,old_pts,None,maxLevel=1,criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,15,0.08))

    cv.circle(mask, (int(new_pts.ravel()[0]),int(new_pts.ravel()[1])), 2 ,(123, 32, 212), 2)
    union = cv.addWeighted(frame2, 0.7, mask, 0.3, 0.1)

    cv.imshow("ekran1",union)

    old_gray = new_gray.copy()
    old_pts = new_pts.copy()

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()