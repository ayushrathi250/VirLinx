import pyautogui

initial_distance = 0
def zoom(results):

    global initial_distance
    zoom_factor = 0.45

    
    if results.multi_hand_landmarks:  # agar hands detect hue to
        for landmarks in results.multi_hand_landmarks:
            # hand check krne ko
            
            handindex = results.multi_hand_landmarks.index(landmarks)

            handdata = results.multi_handedness[handindex].classification
            # handedness = handdata[0].label

            landmarkde = results.multi_hand_landmarks
            if(len(landmarkde) == 2):
                leftindex = landmarkde[0].landmark
                rightindex = landmarkde[1].landmark
                # distance = ((landmark[4].x - landmark[8].x)**2 + (landmark[4].y - landmark[8].y)**2)**0.3

                distance = ((leftindex[8].x - rightindex[8].x)**2 + (leftindex[8].y - rightindex[8].y)**2)**0.3

                if initial_distance == 0:
                    initial_distance = distance

                zoom_factor = distance / initial_distance

                if zoom_factor > 1.1:
                    pyautogui.hotkey('ctrl', '+')
                    # print("zoom up")
                elif zoom_factor < 0.9:
                    pyautogui.hotkey('ctrl', '-') 
                    # print("zoom down") 

