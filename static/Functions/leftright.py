from pynput.keyboard import Controller, Key
import time
import random
from pyautogui import size

keyboard = Controller()

width, height = size()

prev_z = None


def leftnright(hand_landmarks, fwidth):
    global prev_z, width
    

    if hand_landmarks:
        index_tip = hand_landmarks.landmark[8]
        middle_tip = hand_landmarks.landmark[12]
        thumb_tip = hand_landmarks.landmark[4]
        indexb = hand_landmarks.landmark[5]

        
        
        # if prev_z == None:
        #     prev_z = index_tip.z

        # distance = index_tip.z - prev_z
        diff = middle_tip.y - index_tip.y

        # print(distance)
        # if diff > 0.4:
        #     if 0.0035 < distance < 0.0047:
        #         if index_tip.x * width > (width / 2):
        #             keyboard.tap(Key.right)

        #         if index_tip.x * width < (width / 2):
        #             keyboard.tap(Key.left)
        
        # prev_z = index_tip.z

        dist_thum_indexd = ((indexb.x - thumb_tip.x)**2 + (indexb.y - thumb_tip.y)**2)**0.5


        print(dist_thum_indexd)
        if diff > 0.4:
            if 0.07 < dist_thum_indexd < 0.09:
                if index_tip.x * width > (width / 2):
                    keyboard.tap(Key.right)

                if index_tip.x * width < (width / 2):
                    keyboard.tap(Key.left)


