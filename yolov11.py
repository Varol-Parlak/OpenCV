from ultralytics import YOLO
import cv2
import time
import threading

class CameraStream:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.ret, self.frame = self.cap.read()
        self.stopped = False

    def start(self):
        threading.Thread(target=self.update, args=(), daemon=True).start()
        return self

    def update(self):
        while not self.stopped:
            self.ret, self.frame = self.cap.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
        self.cap.release()

# 1. Load Model
model = YOLO("yolo11s.pt").to("cuda")

# 2. Start Threaded Camera
stream = CameraStream(src=0).start()
prev_time = 0

while True:
    frame = stream.read()
    if frame is None: break

    # 3. Process - verbose=False saves CPU time spent printing
    results = model(frame, stream=True, conf=0.5,iou= 0.3, device="cuda", half=True, imgsz=320, verbose=False)

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # FPS Calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(frame, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("YOLO11 Threaded", frame)
    
    if cv2.waitKey(1) == ord("q"):
        break

stream.stop()
cv2.destroyAllWindows()