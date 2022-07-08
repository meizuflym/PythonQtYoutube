from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
 
 
class Youtube():
 
    def __init__(self):
 
        self.window = QWidget()
 
        self.window.setStyleSheet("background-color: #212121;")
        self.window.setWindowTitle("Youtube")
 
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
 
 
        self.back_btn = QPushButton("<")
        self.back_btn.setMaximumHeight(30)
        self.back_btn.setStyleSheet("background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")
 
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMaximumHeight(30)
        self.forward_btn.setStyleSheet("background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;") 

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
 
        self.browser = QWebEngineView()

        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
 
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
 
        self.browser.setUrl(QUrl("https://www.youtube.com"))
 
        self.window.setLayout(self.layout)
        self.window.show()
 
 
 
app = QApplication([])
window = Youtube()
app.exec_()