from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

class AlertWidget(QWidget):
    def __init__(self, parent=None):
        super(AlertWidget, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Create a layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Create a label to show the message
        self.label = QLabel()
        self.label.setObjectName("AlertWidget")
        self.label.setStyleSheet("background-color: #212121;border-width: 1px;border-style: solid;border-color: #8246fa;color: #8246fa; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
        # Timer for automatic hide
        self.timer = QTimer()
        self.timer.timeout.connect(self.hide)

        # Set initial size and position
        self.adjustSize()
        self.reposition()
    
    def show_message(self, message, duration=3000):
        self.label.setText(message)
        self.adjustSize()
        self.reposition()
        self.show()
        if duration > 0:
            self.timer.start(duration)  # Duration in milliseconds
        else:
            self.timer.stop()
    
    def reposition(self):
        screen_rect = QApplication.primaryScreen().availableGeometry()
        widget_rect = self.geometry()
        new_x = screen_rect.width() - widget_rect.width() - 20
        new_y = screen_rect.height() - widget_rect.height() - 20
        self.move(new_x, new_y)

    def hide_Alert(self):
        self.hide()