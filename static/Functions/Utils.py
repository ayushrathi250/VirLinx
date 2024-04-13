import pyautogui, sys, os, subprocess
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
from pynput.keyboard import Controller, Key
import time



keyboard = Controller()

prev_z = None
width = pyautogui.size()[0]
is_menu_opened = False
is_slidemenu_opened = False
is_MediaMenu_opened = False
is_pdfmenu_opened = False
curr_action = [0, 0, 0, 0, 0]
app = QApplication(sys.argv)

class PopupWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setFixedSize(725, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)


        layout = QHBoxLayout()
        
        button_explorer = QPushButton("{}".format("Open Explorer"))
        button_explorer.setFixedSize(175, 175)
        button_explorer.clicked.connect(self.explorer)
        layout.addWidget(button_explorer)
        layout.addSpacing(20) 
        
        button_volume = QPushButton("{}".format("Media Control"))
        button_volume.setFixedSize(175, 175)
        button_volume.clicked.connect(self.media)
        layout.addWidget(button_volume)
        layout.addSpacing(20) 
        
        button_slideshow = QPushButton("{}".format("Slideshow control"))
        button_slideshow.setFixedSize(175, 175)
        button_slideshow.clicked.connect(self.slidectrl)
        layout.addWidget(button_slideshow)
        layout.addSpacing(20) 
        
        # button_pdfcontrol = QPushButton("{}".format("PDF Control"))
        # button_pdfcontrol.setFixedSize(175, 175)
        # button_pdfcontrol.clicked.connect(self.pdfctrl)
        # layout.addWidget(button_pdfcontrol)
        # layout.addSpacing(20) 
        
        button_closewin = QPushButton("{}".format("Close Menu"))
        button_closewin.setFixedSize(175, 175)
        button_closewin.clicked.connect(self.closemenu)
        layout.addWidget(button_closewin)
        layout.addSpacing(20) 
        
        
        self.setLayout(layout)

    def closemenu(self):
       global is_menu_opened
       print("closewin")
       is_menu_opened = False
       self.close()

    def explorer(self):
        global is_menu_opened
        print("explorer")
        if sys.platform == "windows":
            pyautogui.hotkey('win', 'e')
        elif sys.platform == "linux":
            if os.environ == "gnome":
                subprocess.Popen("nautilus")
            elif os.environ == "xfce":
                subprocess.Popen("thunar")
            elif os.environ == "plasma":
                subprocess.Popen("dolphin")
            else:
                pyautogui.hotkey("win", 'e')
        else:
            pyautogui.hotkey("win", 'e')
            
        is_menu_opened = False
        self.close()

    def media(self):
       global is_menu_opened, is_MediaMenu_opened
       print("media")
       if not is_MediaMenu_opened:
           is_menu_opened = False
           self.close()
           mediamenu.show()
           is_MediaMenu_opened = True


    def slidectrl(self):
       global is_menu_opened, is_slidemenu_opened
       print("slidectrl")
       if not is_slidemenu_opened:
           is_menu_opened = False
           self.close()
           slidemenu.show()
           is_slidemenu_opened = True
       
       

    # def pdfctrl(self):
    #    global is_menu_opened, is_pdfmenu_opened
    #    print("pdfctrl")
    #    if not is_pdfmenu_opened:
    #        is_menu_opened = False
    #        self.close()
    #        pdfmenu.show()
    #        is_pdfmenu_opened = True





class SlideTool(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slide Tools")
        self.setFixedSize(725, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        # self.setFocus()



        layout = QHBoxLayout()
        
        button_fromstart = QPushButton("{}".format("From Start Slide"))
        button_fromstart.setFixedSize(175, 175)
        button_fromstart.clicked.connect(self.fromstart)
        layout.addWidget(button_fromstart)
        layout.addSpacing(20) 
        
        button_currslide = QPushButton("{}".format("From Current Slide"))
        button_currslide.setFixedSize(175, 175)
        button_currslide.clicked.connect(self.fromcurr)
        layout.addWidget(button_currslide)
        layout.addSpacing(20)

        button_esc = QPushButton("{}".format("Esc Slideshow"))
        button_esc.setFixedSize(175, 175)
        button_esc.clicked.connect(self.endshow)
        layout.addWidget(button_esc)
        layout.addSpacing(20) 
        
        button_close = QPushButton("{}".format("Close Menu"))
        button_close.setFixedSize(175, 175)
        button_close.clicked.connect(self.closemenu)
        layout.addWidget(button_close)
        layout.addSpacing(20) 
        
        
        
        
        self.setLayout(layout)

    def fromstart(self):
       global is_slidemenu_opened, is_menu_opened
       print("from start")
       self.close()
       time.sleep(1)
       startslide()
       is_slidemenu_opened = False
       is_menu_opened = False

    def fromcurr(self):
        global is_slidemenu_opened, is_menu_opened
        print("from curr")
        self.close()
        time.sleep(1)
        currslide()
        is_slidemenu_opened = False
        is_menu_opened = False

    def endshow(self):
        global is_slidemenu_opened, is_menu_opened
        print("endshow")
        self.close()
        time.sleep(1)
        escslide()
        is_slidemenu_opened = False
        is_menu_opened = False

    def closemenu(self):
       global is_slidemenu_opened, is_menu_opened
       print("close slide menu")
       
       is_slidemenu_opened = False
       is_menu_opened = False
       self.close()

    

# class PDFTool(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PDF Tool")
#         self.setFixedSize(725, 200)
#         self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
#         self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)



#         layout = QHBoxLayout()
        
#         button_fitwidth = QPushButton("{}".format("Fit to Width"))
#         button_fitwidth.setFixedSize(175, 175)
#         button_fitwidth.clicked.connect(self.widthfit)
#         layout.addWidget(button_fitwidth)
#         layout.addSpacing(20) 
        
#         button_fitpage = QPushButton("{}".format("Fit to Page"))
#         button_fitpage.setFixedSize(175, 175)
#         button_fitpage.clicked.connect(self.pagefit)
#         layout.addWidget(button_fitpage)
#         layout.addSpacing(20) 
        
#         button_close = QPushButton("{}".format("Close Menu"))
#         button_close.setFixedSize(175, 175)
#         button_close.clicked.connect(self.closemenu)
#         layout.addWidget(button_close)
#         layout.addSpacing(20) 
        
        
        
        
#         self.setLayout(layout)

#     def widthfit(self):
#        global is_pdfmenu_opened
#        print("fit width")
       
#        is_pdfmenu_opened = False
#        self.close()

#     def pagefit(self):
#         global is_pdfmenu_opened
#         print("fit page")
#         is_pdfmenu_opened = False
#         self.close()

#     def closemenu(self):
#        global is_pdfmenu_opened
#        print("close pdf menu")
       
#        is_pdfmenu_opened = False
#        self.close()




class MediaMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Menu")
        self.setFixedSize(1125, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        layout = QHBoxLayout()
        
        button_incvol = QPushButton("{}".format("Increase Volume"))
        button_incvol.setFixedSize(175, 175)
        # button_incvol.setIcon(QIcon("static/fontsandicons/volup.svg"))
        # button_incvol.setIconSize(QSize(80, 80))
        # button_incvol.setText("Increase Volume")
        button_incvol.clicked.connect(self.incvol)
        layout.addWidget(button_incvol)
        layout.addSpacing(20) 
        
        button_decvol = QPushButton("{}".format("Decrease Volume"))
        button_decvol.setFixedSize(175, 175)
        button_decvol.clicked.connect(self.decvol)
        layout.addWidget(button_decvol)
        layout.addSpacing(20)

        button_mute = QPushButton("{}".format("Mute"))
        button_mute.setFixedSize(175, 175)
        button_mute.clicked.connect(self.mute)
        layout.addWidget(button_mute)
        layout.addSpacing(20)

        button_play = QPushButton("{}".format("Play/Pause"))
        button_play.setFixedSize(175, 175)
        button_play.clicked.connect(self.playpause)
        layout.addWidget(button_play)
        layout.addSpacing(20)
        
        button_close = QPushButton("{}".format("Close Menu"))
        button_close.setFixedSize(175, 175)
        button_close.clicked.connect(self.closemenu)
        layout.addWidget(button_close)
        layout.addSpacing(20) 
          
        self.setLayout(layout)

    def incvol(self):
       global is_MediaMenu_opened, is_menu_opened
       print("inc vol")
       keyboard.tap(Key.media_volume_up)
       is_MediaMenu_opened = False
       is_menu_opened = False

    def decvol(self):
        global is_MediaMenu_opened, is_menu_opened
        print("dec vol")
        keyboard.tap(Key.media_volume_down)
        is_MediaMenu_opened = False
        is_menu_opened = False

    def mute(self):
        global is_MediaMenu_opened, is_menu_opened
        print("mute")
        keyboard.tap(Key.media_volume_mute)
        is_MediaMenu_opened = False
        is_menu_opened = False

    def playpause(self):
        global is_MediaMenu_opened, is_menu_opened
        print("play/pause")
        self.close()
        time.sleep(1)
        playpause()
        is_MediaMenu_opened = False
        is_menu_opened = False

    def closemenu(self):
       global is_MediaMenu_opened
       print("close volume menu")
       
       is_MediaMenu_opened = False
       self.close()



    


popup = PopupWindow()
slidemenu = SlideTool()
# pdfmenu = PDFTool()
mediamenu = MediaMenu()

def Utilities(hand_landmarks):
    global prev_z, width, is_menu_opened, popup, mediamenu, slidemenu, is_slidemenu_opened, is_pdfmenu_opened, is_MediaMenu_opened
    
    if hand_landmarks:
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]

        distance = ((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)**0.5



        if distance < 0.05 and not is_menu_opened:
            popup.show()
            print("hello {}".format(distance))
            is_menu_opened = True
        

def startslide():
    keyboard.tap(Key.f5)

def currslide():
    keyboard.press(Key.shift)
    keyboard.tap(Key.f5)
    keyboard.release(Key.shift)

def escslide():
    keyboard.tap(Key.esc)
    # pyautogui.press("esc")

def playpause():
    keyboard.tap(Key.media_play_pause)
    # pyautogui.press("playpause")