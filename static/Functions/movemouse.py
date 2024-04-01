import pyautogui
import random


def movemouse(results):
    screen_wid, screen_hgt = pyautogui.size()
    # print(screen_wid, " ", screen_hgt)
    
    prev_x, prev_y = pyautogui.position()
    
    # initial_dist = None

    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            handedness =   results.multi_handedness[results.multi_hand_landmarks.index(hand_landmarks)].classification[0].label

            if handedness == "Left":  
                # landmark = results.multi_hand_landmarks[0].landmark
                # if(landmark[4].x > landmark[8].x):
                #     x,y = int(landmark[8].x * screen_wid), int(landmark[8].y * screen_hgt)

                #     dxi = x - prev_x
                #     dyi = y - prev_y
                
                #     pyautogui.moveRel(dxi, dyi)
                        
                #     prev_x = x
                #     prev_y = y

                lm_list = []
                for lm in hand_landmarks.landmark:
                    lm_list.append((lm.x, lm.y))
                
                thumb_tip = lm_list[4]
                index_tip = lm_list[8]
                if(thumb_tip[0] < index_tip[0]):
                    x,y = int(index_tip[0] * screen_wid), int(index_tip[0] * screen_hgt)

                    dxi = x - prev_x
                    dyi = y - prev_y

                    pyautogui.moveRel(dxi, dyi)

                    prev_x = x
                    prev_y = y


