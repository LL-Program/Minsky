from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from UI.Mainwindow import MainWindow
import sys

if __name__ == "__main__":
    while True:
        QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

        app = QApplication([])
        app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    
        window = MainWindow()
        app.installEventFilter(window.header)
    
        sys.exit(app.exec_())