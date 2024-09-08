from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from UI.Mainwindow import MainWindow
import sys

def Startup():
    QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough) 
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  
    app = QApplication([])
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    window = MainWindow(app=app) 
    app.installEventFilter(window.header)
    window.showFullScreen
    sys.exit(app.exec_())
  
if __name__ == "__main__":
    Startup()