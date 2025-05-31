import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self):
        #initialize Mediapipe hands Module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        """
        Detects hand gesture in the given frame.
        Returns: "open_palm", "fist", or None
        """
        #convert frame to RGB for Mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)


        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                #Draw landmarks on the frame
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                #Simple gesture detection: Check if fingers are extended (open palm) or not (fist)
                landmarks = hand_landmarks.landmark
                if landmarks[8].y < landmarks[6].y: #index finger tip vs. base
                    return "open_palm"
                return "fist"
            return None