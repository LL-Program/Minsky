#Lukas Rennhofer- 24.4.2024 - UIManager
#id_00003


from PyQt5.QtWidgets import (QDesktopWidget)
from PyQt5.QtGui import QFont
from UI.statusbar import set_up_status_bar
from PyQt5.QtCore import Qt
import os
import sys

theme = "UI/dark.qss"

def init_ui(MainWindow):
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowTitle(MainWindow.app_name)
        MainWindow.resize(1300, 900)
        center(MainWindow)
        MainWindow.showFullScreen()
	
        MainWindow.setStyleSheet(open(os.path.join(sys.path[0], theme), "r").read())
	
        
        MainWindow.window_font = QFont("Zed Mono Extended", 12)
        MainWindow.setFont(MainWindow.window_font)
        
        MainWindow.setUpBody()
        MainWindow.setMouseTracking(True)
        set_up_status_bar(MainWindow)

        MainWindow.show()

def center(MainWindow):
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())