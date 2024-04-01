# Controlling PC via Hand Gestures using Virlinx, OpenCV, and MediaPipe

## Introduction

This project demonstrates how to control a PC using hand gestures detected through a webcam. We'll be using Virlinx for communication between the hand gesture detection module and the PC, and we'll implement the gesture detection using OpenCV and MediaPipe.

## Requirements

- Python 3.x
- Virlinx
- OpenCV
- MediaPipe
- Webcam

## Setup

1. Install Python 3.x if you haven't already.
2. Install Virlinx, OpenCV, and MediaPipe using pip:
    ```bash
    pip install virlinx opencv-python mediapipe
    ```
3. Ensure you have a webcam connected to your PC.

## Usage

1. Clone or download the repository containing the source code for this project.
2. Navigate to the project directory in your terminal or command prompt.

3. Run the following command to start the hand gesture recognition module:

    ```bash
    python gesture_recognition.py
    ```

4. Once the hand gesture recognition module is running, you can perform various gestures in front of your webcam to control your PC.

## Supported Gestures

- **Swipe Left**: Move to the previous slide (if presenting).
- **Swipe Right**: Move to the next slide (if presenting).
- **Swipe Up**: Move PDF up.
- **Swipe Down**: Move PDF down.
- **Two finger zoom**: Zooming PDF and PPTs.

## Conclusion

By following the steps outlined in this guide, you should be able to control your PC using hand gestures detected through your webcam. This project demonstrates the integration of Virlinx with OpenCV and MediaPipe to create a hands-free interaction experience.
