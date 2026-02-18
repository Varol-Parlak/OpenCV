import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

base_options = python.BaseOptions(model_asset_path='ml/blaze_face_short_range.tflite')
options = vision.FaceDetectorOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO
)
prev_time = 0

def calculate_iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[0] + boxA[2], boxB[0] + boxB[2])
    yB = min(boxA[1] + boxA[3], boxB[1] + boxB[3])
    
    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = boxA[2] * boxA[3]
    boxBArea = boxB[2] * boxB[3]
    
    iou = interArea / float(boxAArea + boxBArea - interArea) if (boxAArea + boxBArea - interArea) > 0 else 0
    return iou

with vision.FaceDetector.create_from_options(options) as detector:
    cap = cv2.VideoCapture(0)
    prev_box = None
    last_iou = 0.0
    frame_count = 0     

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        timestamp_ms = int(time.time() * 1000)
        
        result = detector.detect_for_video(mp_image, timestamp_ms)

        if result.detections:
            b = result.detections[0].bounding_box
            curr_box = [b.origin_x, b.origin_y, b.width, b.height]

            if prev_box is not None:
                    iou_score = calculate_iou(prev_box, curr_box)
                    color = (0, 255, 0) if iou_score > 0.9 else (0, 0, 255)
                    cv2.putText(frame, f"IoU: {iou_score:.2f}", (b.origin_x, b.origin_y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    
            cv2.rectangle(frame, (b.origin_x, b.origin_y), 
                            (b.origin_x + b.width, b.origin_y + b.height), (255, 0, 0), 2)
            prev_box = curr_box
        else:
             prev_box = None
        
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        
        cv2.putText(frame, f"FPS: {int(fps)}", (20, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break


cv2.destroyAllWindows()
cap.release()
