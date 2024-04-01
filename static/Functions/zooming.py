import pyautogui

initial_distance = 0
flag = False
def zoom(results):

    global initial_distance
    zoom_factor = 0.3

    
    if results.multi_hand_landmarks:  # agar hands detect hue to
        for landmarks in results.multi_hand_landmarks:
            # hand check krne ko
            
            handindex = results.multi_hand_landmarks.index(landmarks)

            handdata = results.multi_handedness[handindex].classification
            handedness = handdata[0].label

            if(handedness == "Right"):
                thumb_tip = landmarks.landmark[4]
                index_tip = landmarks.landmark[8]
                middle_tip = landmarks.landmark[20]

                dist_thumb_index = ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)**0.5
                dist_thumb_middle = ((thumb_tip.x - middle_tip.x)**2 + (thumb_tip.y - middle_tip.y)**2)**0.5

                threshold_dist = 0.1
                global flag
                if(dist_thumb_index < threshold_dist):
                    flag = False
                    print("stop zooming")
                elif(dist_thumb_middle < threshold_dist):
                    flag = True
                    print("start zooming")
 
            if flag == True:
                landmarkde = results.multi_hand_landmarks
                if(len(landmarkde) == 2):
                    leftindex = landmarkde[0].landmark
                    rightindex = landmarkde[1].landmark
                    distance = ((leftindex[8].x - rightindex[8].x)**2 + (leftindex[8].y - rightindex[8].y)**2)**0.5

                    if initial_distance == 0:
                        initial_distance = distance

                    zoom_factor = distance / initial_distance

                    if zoom_factor > 1.1:
                        pyautogui.hotkey('ctrl', '+')

                    elif zoom_factor < 0.9:
                        pyautogui.hotkey('ctrl', '-')  
                    
            else:
                pass