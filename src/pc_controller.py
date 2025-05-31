

# pc_controller.py
# Maps gestures to PC actions using PyAutoGUI

import pyautogui

class PCController:
    def __init__(self):
        #configure Pyautogui
        pyautogui.FAILSAFE = True #move mouse top-left to stop
        pyautogui.PAUSE = 0.1 #small dealy between actions

    def control(self, gesture):
        """
        Maps gestures to PC actions.
        - open_palm: Increase volume
        - fist: Decrease volume
        """
        if gesture == "open_palm":
             pyautogui.press("volumeup")
             print("volume Up")
        elif: gesture == "fist":
            pyautogui.press("volumedown")
            print("Volume Down")

        