from pynput.mouse import Controller as MController, Button
from pynput.keyboard import Controller as KController, Key
from pyautogui import size


mouse = MController()
keyboard = KController()
prev_y = None
threshold = 20    
frame_width, frame_height = size()


def scrolling(hand_landmarks, fwidth, fheight):
    global prev_y
    if hand_landmarks:
        index_tip = hand_landmarks.landmark[8]
        middle_tip = hand_landmarks.landmark[12]
        thumb_tip = hand_landmarks.landmark[4]

        # if prev_y == None:
        #     prev_y = middle_tip.y
        # else:
        #     diff = middle_tip.y - index_tip.y
        #     # print(diff)
        #     if -0.04 < diff < 0.04:
        #         distance = middle_tip.y*frame_height - prev_y
        #         print("distance", distance)
        #         # if distance >= 0:
        #         #     mouse.scroll(0, 1)
        #         # elif distance < 0:
        #         #     mouse.scroll(0, -1)

        #         prev_y = middle_tip.y

        diff = middle_tip.y - index_tip.y

        if -0.04 < diff < 0.04:
            if middle_tip.y * fheight < fheight / 2:
                mouse.scroll(0, 1)
                print("up")
            elif middle_tip.y * fheight > fheight / 2:
                mouse.scroll(0, -1)
                print("down")

        