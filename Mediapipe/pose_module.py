import cv2
import mediapipe as mp
import time

class pose_detector():
    
    def __init__(self, mode= False, upBody = False, smooth = True, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode,model_complexity=1,smooth_landmarks=self.smooth,enable_segmentation=False,smooth_segmentation=True,min_detection_confidence=self.detectionCon,min_tracking_confidence=self.trackCon
)

    def find_pose(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(frame, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return frame

    def get_position(self, frame, draw=True):
        lmList = []

        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame, (cx,cy), 10, (255,0,0), -1)

        return lmList

def main():

    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = pose_detector()

    while True:
        ret, frame = cap.read()
        
        frame = detector.find_pose(frame)
        lmList = detector.get_position(frame)

        for lm in lmList:
            print(lm, "\n")
        cTime = time.time()
        fps = int(1 / (cTime - pTime))
        pTime = cTime

        cv2.putText(frame, f"Fps: {fps}", (10,50), cv2.FONT_ITALIC, 2, (255,0,0), 5, cv2.LINE_AA)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break


    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()