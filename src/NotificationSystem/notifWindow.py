from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QPushButton, 
                             QLabel, QGridLayout, QMainWindow)
from PyQt5.QtCore import Qt, QTimer, QSize, QRect
from PyQt5.QtGui import QIcon
import sys

class Message(QWidget):
    def __init__(self, title, message, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold; padding: 0;")
        self.messageLabel = QLabel(message, self)
        self.messageLabel.setStyleSheet("font-size: 12px; font-weight: normal; padding: 0;")
        self.buttonClose = QPushButton(self)
        self.buttonClose.setIcon(QIcon.fromTheme("window-close"))
        self.buttonClose.setFlat(True)
        self.buttonClose.setFixedSize(32, 32)
        self.buttonClose.setIconSize(QSize(16, 16))
        self.layout().addWidget(self.titleLabel)
        self.layout().addWidget(self.messageLabel, 2, 0)
        self.layout().addWidget(self.buttonClose, 0, 1)

class Notification(QWidget):
    def __init__(self, parent = None):        
        super(QWidget, self).__init__(parent = None)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)      
        self.setStyleSheet("background: #d3d7cf; padding: 0;border-radius: 10px;")
        self.mainLayout = QVBoxLayout(self)
        

    def setNotify(self, title, message, timeout):
        self.m = Message(title, message)
        self.mainLayout.addWidget(self.m)
        self.m.buttonClose.clicked.connect(self.onClicked)
        self.show()
        QTimer.singleShot(timeout, 0, self.closeMe)
        
    def closeMe(self):
        self.close()
        self.m.close()
    
    def onClicked(self):
        self.close()
            
class Window(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        btn = QPushButton(QIcon.fromTheme("info"), "show Notify")
        btn.setFixedWidth(110)
        btn.setFixedHeight(30)
        self.setCentralWidget(btn)
        btn.clicked.connect(self.showNotification)
        
    def showNotification(self):
        self.notification = Notification()
        self.notification.setNotify("Emma is calling you", "Message line 1\nMessage line 2\nMessage line 3", 3000)
        r = QRect(self.x() + round(self.width() / 2) - round(self.notification.width() / 2), 
                                        self.y() + 26, self.notification.m.messageLabel.width() + 30, self.notification.m.messageLabel.height())
        self.notification.setGeometry(r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.resize(600, 330)
    w.show()
    sys.exit(app.exec_())