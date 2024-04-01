import sys
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
import multiprocessing
import threading
import app as app2

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VirLinx")
        self.setGeometry(100, 100, 1280, 1024)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:5000"))

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def showEvent(self, event):
        # flask_process.start()
        pass

    def closeEvent(self, event):
        # Stop Flask server by terminating the process
        # app2.running = False
        # flask_process.terminate()
        # flask_process.join()
        pass
        # event.accept()






def start_flask():
    app2.app.run(host="127.0.0.1", port=5000, debug=True)

def run_gui():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    # Check if Flask server is already running
    # flask_process = threading.Thread(target=start_flask)
    # flask_process.start()

    # Run GUI in the main process
    run_gui()
