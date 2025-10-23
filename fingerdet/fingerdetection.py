import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

tip_ids = [8, 12, 16, 20]

video = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hand = mp_hands.Hands()
draw = mp.solutions.drawing_utils

while video.isOpened():
    ret,frame = video.read()

    if ret:
        flip = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(flip,cv2.COLOR_BGR2RGB)
        result = hand.process(rgb)
        if result.multi_hand_landmarks:
            for r in result.multi_hand_landmarks:
                draw.draw_landmarks(flip, r, mp_hands.HAND_CONNECTIONS)
                landmarks = r.landmark
                finger = 0
                if landmarks[4].x < landmarks[3].x:
                        finger+=1
                for i in tip_ids:
                    
                    if landmarks[i].y < landmarks[i-2].y:
                        finger+=1

                cv2.putText(flip,str(finger),(50,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),1,cv2.LINE_AA)
                
        cv2.imshow("Finger Detection",flip)
        if cv2.waitKey(1) == ord("q"):
            break   

video.release()
cv2.destroyAllWindows()
