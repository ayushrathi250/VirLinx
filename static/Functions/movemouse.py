import pyautogui
import random


def movemouse(results):
    screen_wid, screen_hgt = pyautogui.size()
    # print(screen_wid, " ", screen_hgt)
    
    prev_x, prev_y = pyautogui.position()
    
    # initial_dist = None

    
    if results.multi_hand_landmarks:  # agar hands detect hue to
        for landmarks in results.multi_hand_landmarks:
            handedness =   results.multi_handedness[results.multi_hand_landmarks.index(landmarks)].classification[0].label

            if handedness == "Left":  # left mouse
                landmark = results.multi_hand_landmarks[0].landmark
                x,y = int(landmark[8].x * screen_wid), int(landmark[8].y * screen_hgt)

                dxi = x - prev_x
                dyi = y - prev_y

                
                
                pyautogui.moveRel(dxi, dyi)
                # i = 0
                # if(landmark[8].y < landmark[4].y):
                    # print("Left click {}".format(random.randint(1,1000000)))
                    
                prev_x = x
                prev_y = y



