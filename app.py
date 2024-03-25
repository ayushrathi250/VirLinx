import cv2

from static.Functions import movemouse as mvmouse, updown, zooming

import pyautogui as pai
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

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            mvmouse.movemouse(results)
            # updown.updn(results, frame)
            zooming.zoom(results)
                    
            frame = cv2.resize(frame, (0, 0), fx=1.7, fy=2.1)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    finally:
        cap.release()
        cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    