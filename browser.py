import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
import multiprocessing
import app as app2

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VirLinx")
        self.setGeometry(100, 100, 1280, 1024)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:5000"))

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def showEvent(self, event):
        flask_process.start()

    def closeEvent(self, event):
        # Stop Flask server by terminating the process
        app2.running = False
        flask_process.terminate()
        flask_process.join()
        event.accept()

def start_flask():
    app2.app.run(host="127.0.0.1", port=5000, debug=True)

def run_gui():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    # Check if Flask server is already running
    if 'flask_process' not in globals():
        # Set a flag to indicate that the server is running
        app2.running = True
        # Start Flask server in a separate process
        flask_process = multiprocessing.Process(target=start_flask)
        

    # Run GUI in the main process
    run_gui()
