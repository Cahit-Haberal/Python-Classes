import cv2
import mediapipe as mp

class face_detector():

    def __init__(self, minDetectioncon= 0.5,):
        self.minDetectioncon = minDetectioncon

        self.mpFace = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.face = self.mpFace.FaceDetection(self.minDetectioncon)

    def find_face(self, frame, score=True):
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        self.results = self.face.process(rgbFrame)

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                self.mpDraw.draw_detection(frame, detection)
                cx, cy = int(detection.location_data.relative_bounding_box.xmin * w), int(detection.location_data.relative_bounding_box.ymin * h)
                if score:
                    cv2.putText(frame, f"%{int(detection.score[0] * 100)}", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,255), 5)
        
        return frame


def main():
    cap = cv2.VideoCapture(0)
    detector = face_detector()

    while True:
        ret, frame = cap.read()
        frame = detector.find_face(frame)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()