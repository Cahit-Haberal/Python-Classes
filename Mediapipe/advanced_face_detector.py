import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpFace = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
face = mpFace.FaceDetection()

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, c = frame.shape

    results = face.process(rgb)
    
    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(frame, detection)
            
            cx, cy = int(detection.location_data.relative_bounding_box.xmin * w), int(detection.location_data.relative_bounding_box.ymin * h)

            cv2.putText(frame, f"%{int(detection.score[0]* 100)}", (cx,cy), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 5)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()