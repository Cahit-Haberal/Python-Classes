import cv2
import mediapipe as mp
import time
import math

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
length = 0

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb) 

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            for id, lm in enumerate(hand.landmark):
                h, w, c= frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4:
                    tx, ty = cx, cy
                elif id == 8:
                    cv2.line(frame, (tx,ty),(cx,cy), (0,0,255), 2)
                    length = int(math.sqrt((tx - cx) ** 2 + (ty - cy) ** 2))    
                print(id, cx, cy , length,"\n")
            mpDraw.draw_landmarks(frame ,hand, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = int(1/(cTime - pTime))
    pTime = cTime

    frame = cv2.flip(frame, 1)
    cv2.putText(frame, f"fps: {fps}", (0,50), cv2.FONT_ITALIC, 2, (255,0,0), 5)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()