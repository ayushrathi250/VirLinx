from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

prev_x = None


def leftnright(hand_landmarks):
    global prev_x
    

    if hand_landmarks:
        index_tip = hand_landmarks.landmark[8]
        if prev_x == None:
            prev_x = index_tip.x

        distance = index_tip.x - prev_x
        if distance > 0:
            keyboard.tap(Key.right)
            

        elif distance < 0 :
            keyboard.tap(Key.left)

