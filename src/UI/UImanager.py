from PyQt5.QtWidgets import (QDesktopWidget)
from PyQt5.QtGui import QFont,QIcon, QFontDatabase
from UI.statusbar import set_up_status_bar
from PyQt5.QtCore import Qt
from Settings.settings import WINDOW_FONT
from Settings.fontloader import load_fonts
import json
from Settings.datapaths import *
from Settings.StyleManager import find_minskytheme_files,current_theme
from UI.defaultassets import THEMES
def init_ui(MainWindow) -> None:
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowTitle(MainWindow.app_name)
        MainWindow.resize(1300, 900)
        center(MainWindow)
        MainWindow.showFullScreen()
        LoadStyles(MainWindow)
        MainWindow.window_font = QFont(WINDOW_FONT, 12)
        load_fonts()
        MainWindow.setFont(MainWindow.window_font)
        MainWindow.setUpBody()
        MainWindow.setMouseTracking(True)
        set_up_status_bar(MainWindow)
        initWindowLogic(MainWindow)
        MainWindow.show()
def center(MainWindow) -> None:
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
def LoadStyles(MainWindow) -> None:
        MainWindow.setStyleSheet(current_theme[1])
                # themes = find_minskytheme_files(False)
                # for theme in themes:
                #         if uistyle == theme.get('theme_name'):
                #                 theme_file = theme.get('theme_path')+"/"+theme.get('theme_filename')
                #                 if os.path.exists(theme_file):
                #                         with open(theme_file, 'r') as f:
                #                                 stylesheet = f.read()
                #                                 MainWindow.setStyleSheet(stylesheet) 
                #                                 return
                #                 return
                # print("No Style :(")
def initWindowLogic(MainWindow)->None:
        MainWindow.setWindowIcon(QIcon(ICON_PATH+'MinskyLogobig.ico'))