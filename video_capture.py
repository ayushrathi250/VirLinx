import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import pyautogui

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Control")
        layout = QVBoxLayout()
        self.button_play_pause = QPushButton("Play/Pause")
        self.button_play_pause.clicked.connect(self.play_pause)
        layout.addWidget(self.button_play_pause)
        self.setLayout(layout)

    def play_pause(self):
        # Simulate media play/pause keyboard shortcut
        pyautogui.hotkey('shift', 'f5')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
