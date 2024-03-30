import pyautogui


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
                index_tip = lm_list[8]
                
                
                # Check if thumb is above the index finger
                if thumb_tip[1] < index_tip[1]:
                    # Perform swipe up action
                    pyautogui.press('up')
                else:
                    pyautogui.press('down')
            # elif ptip[1]:
            #     pyautogui.press("down")
            # elif thumb_tip[1] < index_tip[1]:
            #     pyautogui.press("a")
            #     print("stop")