import cv2
import mediapipe as mp


class mesh_detector():

    def __init__(self,static_image_mode=False,max_num_faces=1,refine_landmarks=False,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_faces = max_num_faces
        self.refine_landmarks = refine_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpMesh = mp.solutions.face_mesh
        self.mesh = self.mpMesh.FaceMesh(self.static_image_mode, self.max_num_faces, self.refine_landmarks, self.min_detection_confidence, self.min_tracking_confidence)
    
    def mesh_apply(self, frame):
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.mesh.process(rgbFrame)

        if self.results.multi_face_landmarks:
            for facelms in self.results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(frame, facelms, self.mpMesh.FACEMESH_TESSELATION, self.mpDraw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1), self.mpDraw.DrawingSpec(color=(255,0,0), thickness=1))

        return frame

def main():
    cap = cv2.VideoCapture(0)
    detector = mesh_detector()

    while True:
        ret, frame = cap.read()
        frame = detector.mesh_apply(frame)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()