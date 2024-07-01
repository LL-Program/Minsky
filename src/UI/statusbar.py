#Lukas Rennhofer- 24.4.2024 - Statusbar(1)
#id_00001

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
   QStatusBar, QPushButton, QLabel
)
import os,sys
def get_status_button(self, img_path: str, widget) -> QLabel:
        label = QLabel()
        label.setStyleSheet("border: none; padding: 4px;")
        icon = QIcon(img_path)
        label.setPixmap(icon.pixmap(21, 21))
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        label.setFont(self.window_font)
        label.mousePressEvent = lambda e: self.show_hide_tab(e, widget)
        label.setMouseTracking(True)
        label.enterEvent = self.set_cursor_pointer
        label.leaveEvent = self.set_cursor_arrow
        return label
def Statusbarbutton(text, statusbar, action):
        transparent_bg = "background: transparent; border: none;"
        minimize_lbl = QPushButton()
        minimize_lbl.setText(text)
        minimize_lbl.setStyleSheet(transparent_bg)
        minimize_lbl.setCursor(Qt.PointingHandCursor)
        minimize_lbl.clicked.connect(action)
        statusbar.addPermanentWidget(minimize_lbl)
def set_up_status_bar(MainWindow):
        stat = QStatusBar()
        stat.setStyleSheet("color: #D3D3D3;height: 22px;")
        stat.showMessage("Ready", 3000)
       
        copilot_label = get_status_button(MainWindow, os.path.join(sys.path[0], "UI/icons/copilot.svg"), MainWindow.extension_frame)
        labelw = get_status_button(MainWindow,os.path.join(sys.path[0], "UI/icons/project.svg"), MainWindow.file_manager_frame)
        stat.addPermanentWidget(copilot_label, 0)
        stat.addPermanentWidget(labelw, 0)
        
        MainWindow.setStatusBar(stat)