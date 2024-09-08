from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFont

class LogSystem(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setObjectName("MinskyLogSystem")
        self.errorFormat = '<span style="color:red;">{}</span>'
        self.warningFormat = '<span style="color:orange;">{}</span>'
        self.validFormat = '<span style="color:green;">{}</span>'
        self.actionFormat = '<span style="color:blue;">{}</span>'
        self.setFont(QFont("Consolas", 12))
    def addLog(self, text, color):
        self.append(color.format(text))