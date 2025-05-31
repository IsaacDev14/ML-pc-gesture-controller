
# ML PC Gesture Controller

A machine learning-based project that enables you to control your computer using hand gestures detected through your webcam.  
For example, you can increase or decrease the volume by showing specific hand gestures.

---

## Project Overview

This project leverages computer vision and machine learning techniques to recognize hand gestures in real-time and map them to PC control commands such as volume adjustment, media playback, and more.

The system uses:
- **MediaPipe** for hand landmark detection  
- **OpenCV** for webcam video feed handling  
- Custom logic to interpret gestures and trigger system commands

---

## Features

- Real-time hand detection and tracking  
- Gesture recognition to control PC volume  
- Easy to extend for additional gestures and commands  
- Cross-platform (Windows first, with potential support for Linux/Mac)

---

## Getting Started

### Prerequisites

- Python 3.8+ installed on your system  
- Webcam connected and working  
- Windows OS (tested primarily on Windows 10/11)  
- VS Code recommended for editing and running the project  

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ML-pc-gesture-controller.git
   cd ML-pc-gesture-controller
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

Start the main script to test hand gesture detection:

```bash
python main.py
```

---

## Project Structure

```
ML-pc-gesture-controller/
│
├── .gitignore              # Files and folders to ignore in Git commits
├── README.md               # Project overview and setup instructions
├── requirements.txt        # Python packages required to run the project
├── main.py                 # Entry point of the project: hand gesture detection and control logic
├── gestures/               # (Future) Folder for gesture classification and helper scripts
└── utils/                  # (Future) Utilities for system commands and helpers
```

---

## Contributing

Feel free to open issues or submit pull requests to add new gestures and features!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand detection  
- [OpenCV](https://opencv.org/) for computer vision  
- Inspired by gesture control concepts and open-source projects
