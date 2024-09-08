from PyQt5.QtWidgets import QFrame,QLabel
from PyQt5.QtGui import QFont

def get_frame() -> QFrame:
        frame = QFrame()
        frame.setObjectName("MinskyFrame")
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Plain)
        frame.setContentsMargins(1, 1, 1, 1)
        return frame
def create_label(text, style_sheet, alignment, font="Consolas", font_size=15, min_height=200) -> QLabel:
    lbl = QLabel(text)
    lbl.setAlignment(alignment)
    lbl.setFont(QFont(font, font_size))
    lbl.setStyleSheet(style_sheet)
    lbl.setContentsMargins(0, 0, 0, 0)
    lbl.setMaximumHeight(min_height)
    return lbl