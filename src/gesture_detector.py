import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self):
        # Initialize Mediapipe hands module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        """
        Detects hand gesture in the given frame.
        Returns: "open_palm", "fist", or None
        """

        # Convert frame to RGB because Mediapipe expects RGB input
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        # If hand landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Custom drawing of landmarks and connections
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),  # green dots
                    self.mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2)  # blue lines
                )

                # Get frame height and width to map landmark to pixel positions
                h, w, _ = frame.shape

                # Get coordinates of landmark 4 (thumb tip)
                x4 = int(hand_landmarks.landmark[4].x * w)
                y4 = int(hand_landmarks.landmark[4].y * h)
                cv2.circle(frame, (x4, y4), 10, (255, 255, 0), cv2.FILLED)  # Yellow filled circle

                # Get coordinates of landmark 8 (index finger tip)
                x8 = int(hand_landmarks.landmark[8].x * w)
                y8 = int(hand_landmarks.landmark[8].y * h)
                cv2.circle(frame, (x8, y8), 10, (0, 0, 255), cv2.FILLED)  # Red filled circle

                # Simple gesture detection based on index finger tip position
                landmarks = hand_landmarks.landmark
                if landmarks[8].y < landmarks[6].y:
                    return "open_palm"
                return "fist"

        return None
