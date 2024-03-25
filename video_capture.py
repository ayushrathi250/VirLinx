import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
zoom_factor = 0.45
prev_y = 0
# Open webcam
initial_distance = 0
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    # Convert the image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the image with MediaPipe Hands
    results = hands.process(frame_rgb)
    
    # if results.multi_hand_landmarks:
    #     for hand_landmarks in results.multi_hand_landmarks:
    #         # Draw landmarks and connections on the hand
    #         mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    #         handdata = results.multi_handedness[results.multi_hand_landmarks.index(hand_landmarks)].classification
    #         handedness =   handdata[0].label
    #         # print(results.multi_handedness[results.multi_hand_landmarks.index(hand_landmarks)])

    #         if()
 
    if results.multi_hand_landmarks:  # agar hands detect hue to
        for landmarks in results.multi_hand_landmarks:
            # hand check krne ko
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            handindex = results.multi_hand_landmarks.index(landmarks)

            handdata = results.multi_handedness[handindex].classification
            handedness = handdata[0].label

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
                    # pyautogui.hotkey('ctrl', '+')
                    print("zoom up")
                elif zoom_factor < 0.9:
                    # pyautogui.hotkey('ctrl', '-') 
                    print("zoom down")


    # return frame_rgb
    cv2.imshow('Hand Tracking', frame)
        
    
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()