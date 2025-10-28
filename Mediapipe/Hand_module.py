import cv2
import mediapipe as mp
import time
import numpy as np
import math

class hand_detector():
    
    def __init__(self, static_image_mode=False,max_num_hands=2,model_complexity=1,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.mpDraw = mp.solutions.drawing_utils
        self.hands = self.mpHands.Hands(self.static_image_mode, self.max_num_hands, self.model_complexity, self.min_detection_confidence, self.min_tracking_confidence)

    def hand_finder(self, frame):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                for id, lm in enumerate(hand.landmark):
                    self.mpDraw.draw_landmarks(frame, hand, self.mpHands.HAND_CONNECTIONS)
        
        return frame
    
    def hand_position(self, frame, draw=True):
        h, w, c = frame.shape
        minx, maxx = math.inf, 0
        miny, maxy = math.inf, 0
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        lmList = []

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                for id, lm in enumerate(hand.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                    if draw:
                        minx, maxx = cx if cx < minx else minx, cx if cx > maxx else maxx
                        miny, maxy = cy if cy < miny else miny, cy if cy > maxy else maxy

        if minx != math.inf:
            cv2.rectangle(frame, (minx, miny), (maxx, maxy), (0,255,0), 5)
        return lmList
    
    def fingers_up(self, frame):
        detect = hand_detector()
        lmList = detect.hand_position(frame, draw=False)
        UPlist = np.zeros([5])

        if len(lmList) != 0:
            if lmList[8][2] < lmList[6][2]:
                UPlist[0] = 1
            if lmList[12][2] < lmList[10][2]:
                UPlist[1] = 1
            if lmList[16][1] > lmList[14][1]:
                UPlist[2] = 1
            if lmList[20][2] < lmList[18][2]:
                UPlist[3] = 1
            if (lmList[4][1] - lmList[2][1]) > 50:
                UPlist[4] = 1
        
        return UPlist
                    
    
def main():
    cap = cv2.VideoCapture(0)

    pTime = 0
    cTime = 0

    detector = hand_detector()

    while True:
        ret, frame = cap.read()

        frame = detector.hand_finder(frame)
        lmList = detector.hand_position(frame)

        if len(lmList) != 0:
            print(lmList[0])
        cTime = time.time()
        fps = int(1/(cTime - pTime))
        pTime = cTime

        frame = cv2.flip(frame, 1)
        cv2.putText(frame, f"fps: {fps}", (0,50), cv2.FONT_ITALIC, 2, (255,0,0), 5)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()