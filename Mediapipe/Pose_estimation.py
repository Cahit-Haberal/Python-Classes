import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

pTime = 0

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(rgb)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame, (cx,cy), 50, (255,0,0), -1)

    #fps
    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    pTime = cTime

    cv2.putText(frame, f"Fps: {fps}", (10,50), cv2.FONT_ITALIC, 2, (255,0,0), 5, cv2.LINE_AA)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()