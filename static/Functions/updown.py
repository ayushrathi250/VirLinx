import pyautogui as pai


def updn(results, frame):  
    prev_y = pai.position()[1]
    gesture_threshold = 30        
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            handedness =   results.multi_handedness[results.multi_hand_landmarks.index(hand_landmarks)].classification[0].label

            if handedness == "Right":
                landmark = results.multi_hand_landmarks[0].landmark
                index_finger_y = landmark[8].y * frame.shape[0]
                
                # Detect swipe-up gesture on the index finger
                # global prev_y
                if prev_y != 0 and index_finger_y < prev_y - gesture_threshold:
                    # print("Hello {}".format(i+1))  # Print "Hello" when swipe-up gesture is detected
                    pai.press("up")
                elif prev_y != 0 and index_finger_y > prev_y - gesture_threshold:
                    pai.press("down")
                    
                prev_y = index_finger_y