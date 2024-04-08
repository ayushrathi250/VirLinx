import cv2
import mediapipe as mp
import numpy as np

class DrawingCanvas:
    def __init__(self, width, height):
        self.canvas = np.ones((height, width, 3), dtype=np.uint8) * 255 # White canvas
        self.drawing = False
        self.last_point = None

    def clear_canvas(self):
        self.canvas.fill(255)  # Reset canvas to white

    def save_canvas(self, filename):
        cv2.imwrite(filename, self.canvas)

    def draw_on_canvas(self, point):
        if self.last_point is not None:
            cv2.line(self.canvas, self.last_point, point, (0, 255, 0), thickness=5)
        self.last_point = point

    def reset_last_point(self):
        self.last_point = None

def main():
    prev_x, prev_y = None, None
    # canvas = DrawingCanvas(width, height)
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

    while True:
        # Check for keyboard input
        

        # Process hand landmarks
        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)
        canvas = frame.copy()
        width, height, _ = frame.shape
        processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(processed_frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                index_tip = hand_landmarks.landmark[8]

                x, y = int(index_tip.x * width), int(index_tip.y * height)
                if(prev_x == None and prev_y == None):
                    prev_x = x
                    prev_y = y
                frame = cv2.line(canvas,pt1=(prev_x, prev_y), pt2=(x, y), color=(0, 255, 0), thickness=5)
                
            
            prev_x = x
            prev_y = y
                

        cv2.imshow('Canvas', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
