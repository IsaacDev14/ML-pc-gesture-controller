# tests/test_gestures.py
# Unit tests for GestureDetector class

import unittest
import cv2
import numpy as np
from src.gesture_detector import GestureDetector

class TestGestureDetector(unittest.TestCase):
    def setUp(self):
        self.detector = GestureDetector()

    def test_initialization(self):
        """Test that GestureDetector initializes correctly."""
        self.assertIsNotNone(self.detector.mp_hands)
        self.assertIsNotNone(self.detector.hands)
        self.assertIsNotNone(self.detector.mp_draw)

    def test_detect_no_hand(self):
        """Test gesture detection with no hand in frame."""
        # Create a blank image (no hand)
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        result = self.detector.detect(frame)
        self.assertIsNone(result, "Expected None for no hand detected")

if __name__ == "__main__":
    unittest.main()