# pc_controller.py
# Maps gestures to PC actions using PyAutoGUI

import pyautogui

class PCController:
    def __init__(self):
        # Configure PyAutoGUI
        pyautogui.FAILSAFE = True  # Move mouse to top-left to stop
        pyautogui.PAUSE = 0.1  # Small delay between actions

    def control(self, gesture):
        """
        Maps gestures to PC actions.
        - open_palm: Increase volume
        - fist: Decrease volume
        """
        if gesture == "open_palm":
            pyautogui.press("volumeup")
            print("Volume Up")
        elif gesture == "fist":
            pyautogui.press("volumedown")
            print("Volume Down")