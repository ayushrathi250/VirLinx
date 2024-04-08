from pynput.mouse import Controller, Button
from pyautogui import size

mouse = Controller()

def movemouse(hand_landmarks):
    
    frame_width, frame_height = size()
    threshold_dist = 0.1
    if hand_landmarks:
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]
        middle_tip = hand_landmarks.landmark[12]
        indexd = hand_landmarks.landmark[6]

        x = int(index_tip.x * frame_width)
        y = int(index_tip.y * frame_height)
        mouse.position = (x, y)
        
        dist_indexd_thumb = ((indexd.x - thumb_tip.x)**2 + (indexd.y - thumb_tip.y)**2)**0.5


        if dist_indexd_thumb < 0.065:
            mouse.click(Button.left)

        

        

