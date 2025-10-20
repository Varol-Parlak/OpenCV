import cv2
import time 
import serial.tools.list_ports 
import mediapipe as mp


def find_hands(frame, draw = True):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(frame)
    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            if draw:
                mp_draw.draw_landmarks(rgb_frame, i, mp_hands.HAND_CONNECTIONS)
    return rgb_frame , result
            
def find_position(frame, results, hand_no=0, draw=True):
    lm_list = []
    if results.multi_hand_landmarks:
        my_hand = results.multi_hand_landmarks[hand_no]
        for id, lm in enumerate(my_hand.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append([id,cx,cy])
            if draw:
                cv2.circle(frame, (cx,cy),50,(255,0,0),-1)
    return lm_list 

finger_tips = [4,8,12,16,20]

cap = cv2.VideoCapture(0)

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils 
pTime = 0

serialInst.baudrate = 9600
serialInst.port = "COM5"
serialInst.open()

last_count = None  

while True:
    _, frame = cap.read()
    #fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame, f'Fps: {int(fps)}', (10,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0), 3,cv2.LINE_AA)

    rgb_frame, results = find_hands(frame)
    landmarks = find_position(rgb_frame,results,draw=False)

    if len(landmarks) != 0:
        fingers_status= []

        if landmarks[finger_tips[0]][1] > landmarks[finger_tips[0] - 1 ] [1]:
            fingers_status.append(1)
        else:
            fingers_status.append(0)

        for finger in range (1,5):
            if landmarks[finger_tips[finger]][2] < landmarks[finger_tips[finger] - 2][2]:
                fingers_status.append(1)
            else:
                fingers_status.append(0)

        total_count = fingers_status.count(1)
        cv2.putText(rgb_frame, str(total_count), (0,420),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),4)

        if total_count != last_count:
            if total_count == 1:
                serialInst.write(1) 
                print("gönder 1")
                
            elif total_count == 2:
                serialInst.write(w)  
                
                print("gönder 2")
            last_count = total_count
        

    norm = cv2.cvtColor(rgb_frame,cv2.COLOR_RGB2BGR)
    cv2.imshow("image", norm)

    if cv2.waitKey(1) == ord("q"):
        break


serialInst.close()
