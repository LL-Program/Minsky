#Lukas Rennhofer- 24.4.2024 - Statusbar(1)
#id_00001
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
   QStatusBar, QPushButton, QLabel
)
from Settings.datapaths import ICON_PATH

def get_status_button(self, img_path: str, widget,Tooltip : str) -> QLabel:
        label = QLabel()
        label.setStyleSheet("border: none; padding: 4px;")
        icon = QIcon(img_path)
        label.setToolTip(Tooltip)
        label.setPixmap(icon.pixmap(21, 21))
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        label.setFont(self.window_font)
        label.mousePressEvent = lambda e: self.show_hide_tab(e, widget)
        label.setMouseTracking(True)
        label.enterEvent = self.set_cursor_pointer
        label.leaveEvent = self.set_cursor_arrow 
        return label
def Statusbarbutton(text, statusbar, action) -> None:
        minimize_lbl = QPushButton()
        minimize_lbl.setText(text)
        minimize_lbl.setObjectName("MinskyStatusBarbutton")
        minimize_lbl.setCursor(Qt.PointingHandCursor)
        minimize_lbl.clicked.connect(action)
        statusbar.addPermanentWidget(minimize_lbl)
def set_up_status_bar(MainWindow) -> None:
        stat = QStatusBar()
        stat.setObjectName("MinskyStatusBar")
        stat.showMessage("Ready", 3000)
        log_label = get_status_button(MainWindow,ICON_PATH +"log.svg", MainWindow.log_frame, "Log System")
        deltasphere_label= get_status_button(MainWindow,ICON_PATH +"deltasphere.svg", MainWindow.Deltasphere_Frame, "DeltaSphereAI")
        search_label = get_status_button(MainWindow,ICON_PATH +"search_icon.svg", MainWindow.search_frame, "Fuzzy Searcher")
        terminal_label = get_status_button(MainWindow, ICON_PATH +"terminal.svg", MainWindow.terminal_frame, "Terminal")
        labelw = get_status_button(MainWindow,ICON_PATH +"project.svg", MainWindow.file_manager_frame, "File Manager")
        stat.addPermanentWidget(log_label, 0)
        stat.addPermanentWidget(deltasphere_label, 0)
        stat.addPermanentWidget(search_label, 0)
        stat.addPermanentWidget(terminal_label, 0)
        stat.addPermanentWidget(labelw, 0)
        MainWindow.setStatusBar(stat)