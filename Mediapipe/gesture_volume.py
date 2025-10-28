import Hand_module, cv2, math, os
import mediapipe as mp


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = Hand_module.hand_detector()

while True:
    ret, frame = cap.read()

    frame = detector.hand_finder(frame)
    lmList = detector.hand_position(frame)
    
    cv2.rectangle(frame, (520,360), (580,120), (0,255,0), 1)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1],lmList[8][2]
        cx, cy = int((x1 + x2) / 2) , int((y1 + y2) / 2)

        cv2.line(frame, (x1, y1), (x2, y2), (255,0,0), 2)
        cv2.circle(frame, (cx, cy), 10, (255,0,0), -1)
        
        length = int((math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))/2.7) if int((math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))/2.7) <= 100 else 100
        print(length)
        
        if length < 8:
            cv2.circle(frame, (cx, cy), 10, (0,255,0), -1)
            os.system("osascript -e 'set volume output volume 0'")
        else:
            os.system(f"osascript -e 'set volume output volume {length}'")
    
    cv2.rectangle(frame, (520,360), (580, 360 - int(length * 2.4)), (0,255,0), -1)
    frame = cv2.flip(frame, 1)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()