import cv2, Hand_module, math
from pynput.mouse import Controller
import numpy as np

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
detector = Hand_module.hand_detector(max_num_hands=1)

cap.set(3, wCam)
cap.set(4, hCam)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    frame = detector.hand_finder(frame)
    lmlist = detector.hand_position(frame)
    up_Fingers = detector.fingers_up(frame)
    cv2.rectangle(frame, (120, 120), (520, 360), (0,255,0), 5)
    if len(lmlist) != 0:
        x8, y8= lmlist[8][1], lmlist[8][2]
        x12, y12 = lmlist[12][1], lmlist[12][2]
        x4, y4 = lmlist[4][1], lmlist[4][2]
        mouse = Controller()
        if 120 < x4 < 520 and 120 < y4 < 360:
            if up_Fingers[0] == 1 and all(x == 0 for x in up_Fingers[1:4]):
                x_screen = np.interp(x8,(120, 520),(0, 2560))
                y_screen = np.interp(y8, (120, 360),(0, 1664))
                mouse.position(x_screen, y_screen)
            elif math.sqrt((x8-x12) ** 2 + (y8 - y12) ** 2) < 80:
                cv2.line(frame, (x8, y8), (x12, y12), (255,0,0), 10)
            elif math.sqrt((x8-x4) ** 2 + (y8 - y4) ** 2) < 50:
                cv2.circle(frame, (int((x4+x8)/2), int((y4+y8)/2)), 30, (0,0,255), -1)
                mouse.click()

    
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()