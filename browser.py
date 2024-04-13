import sys
from PyQt6.QtCore import QUrl, QThread
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import threading
import app as flask_server

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VirLinx")
        self.setGeometry(100, 100, 1280, 1024)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:5000"))

        self.setCentralWidget(self.browser)


        self.flask_thread = FlaskThread()
        self.flask_thread.start()

    def closeEvent(self, event):
        self.flask_thread.stop()
        event.accept()

class FlaskThread(QThread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        start_flask()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def start_flask():
    flask_server.app.run(host="127.0.0.1", port=5000)

if __name__ == "__main__":
    virlinx = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()

    sys.exit(virlinx.exec())
