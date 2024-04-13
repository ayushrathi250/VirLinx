import cv2

import os, signal, sys
from static.Functions import Utils, Scroll, ZoomnPan, leftright, Mouse
from pyautogui import size
import mediapipe as mp

from flask import Flask, Response, render_template
app = Flask(__name__)



def gen_frames():
    # Open the webcam
    
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            results = hands.process(frame_rgb)
            fwidth, fheight, _ = frame.shape

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    handedness =   results.multi_handedness[results.multi_hand_landmarks.index(hand_landmarks)].classification[0].label
                    handsnum = results.multi_hand_landmarks
                    
                    if(len(handsnum) == 1):
                        if handedness == "Left":
                            Utils.Utilities(hand_landmarks)
                            Mouse.movemouse(hand_landmarks)

                        if handedness == "Right":
                            leftright.leftnright(hand_landmarks)
                            Scroll.scrolling(hand_landmarks, fwidth, fheight)

                    elif(len(handsnum) == 2):
                        ZoomnPan.zoom(handsnum, handedness)
                        # print("Hello")
                    
                    
            # frame = cv2.resize(frame, (0, 0), fx=1.7, fy=2.1)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    finally:
        cap.release()
        cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('rndm.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/stopServer')
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    


# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=5000, debug=True)
    