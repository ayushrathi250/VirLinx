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


class MyBar(QWidget):
    def __init__(self, ):
        super(MyBar, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel("My Own Bar")

        btn_size = 35

        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size, btn_size)
        self.btn_close.setStyleSheet("background-color: red;")

        self.btn_min = QPushButton("-")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet("background-color: gray;")

        self.btn_max = QPushButton("+")
        self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet("background-color: gray;")

        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet(
            """
            background-color: black;
            color: white;
        """
        )
        self.setLayout(self.layout)


    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.window().width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        print(event.pos())
        self.end = self.mapToGlobal(event.pos())
        delta = self.end - self.start
        self.window().setGeometry(
            self.mapToGlobal(delta).x(),
            self.mapToGlobal(delta).y(),
            self.window().width(),
            self.window().height(),
        )
        self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.window().close()

    def btn_max_clicked(self):
        self.window().showMaximized()

    def btn_min_clicked(self):
        self.window().showMinimized()



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
