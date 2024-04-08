from pynput.mouse import Controller as MController, Button
from pynput.keyboard import Controller as KController, Key
from pyautogui import size


mouse = MController()
keyboard = KController()
prev_y = None
threshold = 20    
frame_width, frame_height = size()


def scrolling(hand_landmarks):
    global prev_y
    if hand_landmarks:
        middle_tip = hand_landmarks.landmark[12]
        thumb_tip = hand_landmarks.landmark[4]

        if prev_y == None:
            prev_y = middle_tip.y
        else:
            distance = middle_tip.y - prev_y
            if distance >= 0 and thumb_tip.x < middle_tip.x:
                mouse.scroll(0, 1)
            elif distance < 0 and thumb_tip.x < middle_tip.x:
                mouse.scroll(0, -1)

        
