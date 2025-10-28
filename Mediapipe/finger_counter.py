import Hand_module, cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

detector = Hand_module.hand_detector()

while True:
    ret, frame = cap.read()
    finger_count = 0
    frame = detector.hand_finder(frame)
    lmList = detector.hand_position(frame)

    if len(lmList) != 0:
        if lmList[8][2] < lmList[6][2]:
            finger_count += 1
        if lmList[12][2] < lmList[10][2]:
            finger_count += 1
        if lmList[16][1] > lmList[14][1]:
            finger_count += 1
        if lmList[20][2] < lmList[18][2]:
            finger_count += 1
        if (lmList[4][1] - lmList[2][1]) > 50:
            finger_count += 1

    frame = cv2.flip(frame, 1)
    cv2.putText(frame, f"NUM_FINGER: {finger_count}", (0,30), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 5)        
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
