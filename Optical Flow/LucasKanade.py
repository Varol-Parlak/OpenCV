import cv2 as cv
import numpy as np

feature_params = dict(maxCorners=100, qualityLevel=0.3, blockSize=7, minDistance=7)
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

cap = cv.VideoCapture(0)
_, prev = cap.read()
prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)
color = np.random.randint(0, 255, (100, 3), dtype = np.uint8)

p0 = cv.goodFeaturesToTrack(prevgray, mask=None, **feature_params)

mask = np.zeros_like(prev)

while True:
    _, newframe = cap.read()
    newgray = cv.cvtColor(newframe, cv.COLOR_BGR2GRAY)

    p1, st, err = cv.calcOpticalFlowPyrLK(prevgray, newgray, p0, None, **lk_params)

    new_pts = p1[st == 1]
    old_pts = p0[st == 1]

    for i, (new, old) in enumerate(zip(new_pts, old_pts)):
        a, b = new.ravel()
        c, d = old.ravel()
        color_tuple = tuple(map(int, color[i]))
        mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color_tuple, 2)
        newframe = cv.circle(newframe, (int(a), int(b)), 5, color_tuple, -1)

    img = cv.add(newframe, mask)
    cv.imshow("eff", img)

    if cv.waitKey(1) == ord("q"):
        break

    prevgray = newgray.copy()
    p0 = new_pts.reshape(-1, 1, 2)

cap.release()
cv.destroyAllWindows()
