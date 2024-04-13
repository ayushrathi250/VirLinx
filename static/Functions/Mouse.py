from pynput.mouse import Controller, Button
from pyautogui import size

mouse = Controller()

prev_z = None

def movemouse(hand_landmarks):
    global prev_z
    frame_width, frame_height = size()
    threshold_dist = 0.1
    if hand_landmarks:
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]
        middle_tip = hand_landmarks.landmark[12]
        indexd = hand_landmarks.landmark[6]

        x = int(index_tip.x * frame_width * 2) - 0.5
        y = int(index_tip.y * frame_height * 2) - 0.5
        mouse.position = (x, y)
        
        dist_indexd_thumb = ((indexd.x - thumb_tip.x)**2 + (indexd.y - thumb_tip.y)**2)**0.5

        if 0.04 < dist_indexd_thumb < 0.057:
            mouse.click(Button.left)

            # if prev_z is not None:
            #     distance = index_tip.z - prev_z

            #     if 0.015 < distance < 0.035:
            #         mouse.click(Button.left)

            # prev_z = index_tip.z


        

        

