from pynput.mouse import Controller as MController, Button
from pynput.keyboard import Controller as KController, Key
from pyautogui import size
import time


mouse = MController()
keyboard = KController()

prev_y = None
width, height = size()
prevM_x, prevM_y = None, None


def zoom_up():
    keyboard.press(Key.ctrl)
    mouse.scroll(0, 1)
    keyboard.release(Key.ctrl)

def zoom_down():
    keyboard.press(Key.ctrl)
    mouse.scroll(0, -1)
    keyboard.release(Key.ctrl)


def pan(dx, dy):
    if dx>0 and dy>0:
        mouse.scroll(1, -1)
    if dx<0 and dy>0:
        mouse.scroll(-1, -1)
    if dx>0 and dy<0:
        mouse.scroll(1, 1)
    if dx<0 and dy<0:
        mouse.scroll(-1, 1)
    if dx==0 and dy>0:
        mouse.scroll(0, -1)
    if dx==0 and dy<0:
        mouse.scroll(0, 1)
    if dx>0 and dy==0:
        mouse.scroll(1, 0)
    if dx<0 and dy==0:
        mouse.scroll(-1, 0)
    if dx==0 and dy==0:
        mouse.scroll(0, 0)
    



def zoom(hand_landmarks, handeness):
    global prev_y, width, height, prevM_x, prevM_y

    if hand_landmarks:
        Lindex_tip = hand_landmarks[0].landmark[8]
        Lthumb_tip = hand_landmarks[0].landmark[4]
        Lindexd = hand_landmarks[0].landmark[6]

        Rindex_tip = hand_landmarks[1].landmark[8]
        Rthumb_tip = hand_landmarks[1].landmark[4]
        Rindexd = hand_landmarks[1].landmark[6]

        if handeness == "Right":
            Rdistance = (((Rthumb_tip.x - Rindexd.x))**2 + ((Rthumb_tip.y - Rindexd.y))**2)**0.5

            if Rdistance < 0.05:

                if prev_y is not None:
                    change = (Rindex_tip.y * height) - prev_y

                    if change > 10:
                        zoom_up()
                    elif change < -10:
                        zoom_down()
                
                prev_y = Rindex_tip.y * height


        if handeness == "Left":
            Ldistance = (((Lthumb_tip.x - Lindexd.x))**2 + ((Lthumb_tip.y - Lindexd.y))**2)**0.5

            currM_x, currM_y = int(Lindex_tip.x * width / 2), int(Lindex_tip.y * height)
            if Ldistance < 0.05:
                if prevM_x is not None and prevM_y is not None:
                    dx = currM_x - prevM_x
                    dy = currM_y - prevM_y

                    pan(dx, dy)

                prevM_x, prevM_y = currM_x, currM_y