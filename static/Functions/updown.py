import pyautogui
import time

def updn(results, frame):  
    prev_y = pyautogui.position()[1]
    gesture_threshold = 30        
    # if results.multi_hand_landmarks:
    #     for hand_landmarks in results.multi_hand_landmarks:


    #             landmark = results.multi_hand_landmarks[0].landmark
    #             index_finger_y = landmark[8].y * frame.shape[0]
                
    #             # Detect swipe-up gesture on the index finger
    #             # global prev_y
    #             if prev_y != 0 and index_finger_y < prev_y - gesture_threshold:
    #                 # print("Hello {}".format(i+1))  # Print "Hello" when swipe-up gesture is detected
    #                 pai.press("down")
    #             # elif prev_y != 0 and index_finger_y > prev_y - gesture_threshold:
    #             #     pai.press("down")
                    
    #             prev_y = index_finger_y

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            handedness =   results.multi_handedness[results.multi_hand_landmarks.index(hand_landmarks)].classification[0].label
            
            if handedness == "Right":

                lm_list = []
                for lm in hand_landmarks.landmark:
                    lm_list.append((lm.x, lm.y))
                
                thumb_tip = lm_list[4]
                indexd_tip = lm_list[8]
                middled_tip = lm_list[12]
                threshold_val = 0.05
                
                dist_th_ind = ((thumb_tip[0] - indexd_tip[0])**2 + (thumb_tip[1] - indexd_tip[1])**2)**0.5
                dist_th_inp = ((thumb_tip[0] - middled_tip[0])**2 + (thumb_tip[1] - middled_tip[1])**2)**0.5
                if dist_th_ind < threshold_val:
                    pyautogui.press('up')
                    # break
                elif dist_th_inp < threshold_val:
                    pyautogui.press('down')
                    # break
