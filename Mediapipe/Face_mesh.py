import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpDraw = mp.solutions.drawing_utils
mpMesh = mp.solutions.face_mesh
mesh = mpMesh.FaceMesh(max_num_faces=2)

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mesh.process(rgb)
    
    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame,facelms, mpMesh.FACEMESH_TESSELATION, mpDraw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1), mpDraw.DrawingSpec(color=(255,0,0), thickness=1))

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()