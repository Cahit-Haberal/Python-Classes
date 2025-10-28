import Hand_module, cv2
import math
import numpy as np

cap = cv2.VideoCapture(0)
detector = Hand_module.hand_detector()
color = np.array([255,0,0])
new_list = []
color_name = "NONE"
tuval = np.zeros([1080, 1920, 3])
while True:
    ret, frame = cap.read()
    frame = detector.hand_finder(frame)
    lmList = detector.hand_position(frame)
    #upFingers = detector.fingers_up(frame)

    cv2.rectangle(frame, (100,50), (250,200), (0,0,255), -1)
    cv2.rectangle(frame, (100,250), (250,400), (255,0,0), -1)
    cv2.rectangle(frame, (100,450), (250,600), (0,255,0), -1)
    cv2.rectangle(frame, (100,650), (250,800), (0,0,0), 5)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[12][1], lmList[12][2]
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

        if distance <= 120 and cy < 1920:
            if 100 < cx < 250 and 50 < cy < 200:
                color = np.array([0,0,255])
                color_name = "RED"
            elif 100 < cx < 250 and 250 < cy < 400:
                color = np.array([255,0,0])
                color_name = "BLUE"
            elif 100 < cx < 250 and 450 < cy < 600:
                color = np.array([0,255,0])
                color_name = "GREEN"
            elif 100 < cx < 250 and 650 < cy < 800:
                color_name = "ERASE"
            else:
                if color_name == "ERASE":   
                    for id, pos in enumerate(new_list):
                        if abs(cx - pos[0]) < 125 and abs(cy - pos[1]) < 125:
                            new_list.pop(id)
                else:
                    new_list.append([cx, cy, color])

   
        
    if len(new_list) != 0:
        for tx , ty, clr in new_list:
            cv2.circle(frame, (tx, ty), 50, tuple(clr.tolist()), -1)

    frame = cv2.flip(frame, 1)
    tuval = cv2.flip(tuval, 1)
    #cv2.putText(frame, f"{upFingers}", (10,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
    cv2.putText(frame, f"COLOR: {color_name}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
    cv2.imshow("Frame", frame)
    cv2.imshow("Canvas", tuval)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()