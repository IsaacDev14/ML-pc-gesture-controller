import cv2
from gesture_detector import GestureDetector
from pc_controller import PCController

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    detector = GestureDetector()
    controller = PCController()
    print("Starting gesture controller. Press 'q' to quit.")

    paused = False  # ✅ NEW: Track paused state

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gesture = detector.detect(frame)

        # ✅ NEW: Toggle pause
        if gesture == "pause_toggle":
            paused = not paused
            state = "PAUSED" if paused else "RESUMED"
            print(f"[{state}] Gesture control is now {state.lower()}.")
        
        # ✅ Only control PC if not paused
        elif not paused:
            controller.control(gesture)

        cv2.imshow("Gesture Controller", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
