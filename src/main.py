# main.py
# Entry point for the ML PC Gesture Controller
# Initializes webcam, detects gestures, and controls PC actions

import cv2
from gesture_detector import GestureDetector
from pc_controller import PCController

def main():
    #initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    #initializing gesture detectoe and pc controller
    detector = GestureDetector()
    controller = PCController()
    print("Stating gesture controller. press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        #Detect gesture
        gesture = detector.detect(frame)

        #Control Pc based on gesture
        controller.control(gesture)

        #display the frame
        cv2.imshow("Gesture Controller", frame)

        #Quit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    #cleanup
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()