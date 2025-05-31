import cv2
import mediapipe as mp
import math

class GestureDetector:
    def __init__(self):
        # Initialize Mediapipe hands module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.paused = False  # Pause flag

    def detect(self, frame):
        """
        Detects hand gesture in the given frame.
        Returns: "open_palm", "fist", "pause", or None
        """

        # Convert frame to RGB (required by Mediapipe)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks and connections with custom colors
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),  # green dots
                    self.mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2)  # blue lines
                )

                # Get frame size
                h, w, _ = frame.shape

                # Get thumb tip coordinates (landmark 4)
                x4 = int(hand_landmarks.landmark[4].x * w)
                y4 = int(hand_landmarks.landmark[4].y * h)

                # Get index finger tip coordinates (landmark 8)
                x8 = int(hand_landmarks.landmark[8].x * w)
                y8 = int(hand_landmarks.landmark[8].y * h)

                # Draw circles on thumb tip and index finger tip
                cv2.circle(frame, (x4, y4), 10, (255, 255, 0), cv2.FILLED)  # Yellow
                cv2.circle(frame, (x8, y8), 10, (0, 0, 255), cv2.FILLED)    # Red

                # Draw line between thumb and index finger
                cv2.line(frame, (x4, y4), (x8, y8), (0, 255, 255), 2)  # Yellow line

                # Calculate midpoint of the line
                mid_x = (x4 + x8) // 2
                mid_y = (y4 + y8) // 2

                # Draw a white dot at the midpoint
                cv2.circle(frame, (mid_x, mid_y), 5, (255, 255, 255), cv2.FILLED)

                # Calculate distance between thumb and index finger tips
                distance = int(math.hypot(x8 - x4, y8 - y4))

                # Display distance on the frame near the midpoint
                cv2.putText(frame, f"{distance}px", (mid_x + 10, mid_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

                landmarks = hand_landmarks.landmark

                # Pause gesture: toggle pause if thumb is up (tip above base)
                if landmarks[4].y < landmarks[3].y:
                    self.paused = not self.paused
                    print("Paused" if self.paused else "Resumed")
                    return "pause"

                # If paused, do not detect other gestures
                if self.paused:
                    return None

                # Detect open palm or fist based on index finger tip position
                if landmarks[8].y < landmarks[6].y:
                    return "open_palm"
                return "fist"

        return None
