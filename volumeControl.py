import cv2
import matplotlib.pyplot as plt
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume  # Direct access to the volume interface
volRange = volume.GetVolumeRange() 
minVol, maxVol = volRange[0], volRange[1]

video = cv2.VideoCapture(0)
tx, ty, ix, iy = 0, 0, 0, 0
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()
draw = mp.solutions.drawing_utils

while video.isOpened():
    ret,frame = video.read()

    if ret:
        flip = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(flip,cv2.COLOR_BGR2RGB)
        result = hand.process(rgb)
        heigth, width, _ = frame.shape
        if result.multi_hand_landmarks:
            for i in result.multi_hand_landmarks:    
                for id, r in enumerate(i.landmark):
                    if id == 4:
                        tx, ty = int(r.x * width), int(r.y * heigth)
                        cv2.circle(flip, (tx, ty), 8, (0, 255, 0), -1) 
                    elif id == 8:
                        ix, iy = int(r.x * width), int(r.y * heigth)
                        cv2.circle(flip, (ix, iy), 8, (0, 255, 0), -1) 
            cv2.line(flip, (tx, ty), (ix, iy), (255, 0, 0), 3, cv2.LINE_AA)
            
            dx, dy = ix - tx, iy - ty
            distance = math.hypot(dx, dy) 
            vol = np.interp(distance, [50, 200], [0.0, 1.0])       
            
            volume.SetMasterVolumeLevelScalar(vol, None)

        cv2.imshow("Finger Detection",flip)
        if cv2.waitKey(1) == ord("q"):
            break   

video.release()
cv2.destroyAllWindows()
