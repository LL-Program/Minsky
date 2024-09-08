import sys
from PyQt5.QtCore import QProcess, Qt, QTimer, QSize
from PyQt5.QtWidgets import QTextEdit, QWidget, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem, QStackedWidget, QVBoxLayout,QFrame,QLabel
from PyQt5.QtGui import QTextCursor, QFont,  QPainter, QPalette, QImage, QPixmap,QIcon
from Settings.datapaths import *

class Heading(QFrame):
    def __init__(self, Terminal) -> None:
        super().__init__(None)
        self.terminal = Terminal
        self.setFixedHeight(45)
        self.setObjectName("TermianlHeading")
        # Layout setup
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(4, 0, 4, 0)
        main_layout.setSpacing(10)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Button setup
        self.plus_icon = QIcon(ICON_PATH+'plus.svg')  # Update path as needed
        btn_size = QSize(15, 15)

        close_btn = QPushButton()
        close_btn.setIcon(self.plus_icon)
        close_btn.setIconSize(btn_size)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        close_btn.setStyleSheet("background: transparent; border: none;")
        close_btn.clicked.connect(self.terminal.add_Terminal)

        # Add button to layout
        main_layout.addWidget(close_btn)
class TerminalWidget(QTextEdit):
    def __init__(self,main_window):
        super().__init__()
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)  # Merge stdout and stderr
        self.process.readyRead.connect(self.readOutput)
        self.startShell()
        self.main_window = main_window
        self.prompt = ""
        self.commandHistory = []
        self.historyIndex = -1
        self.command_start_position = self.textCursor().position()
        self.setObjectName("CodeTerminal")
        self.cursor_rect = self.cursorRect()
        self.cursor_rect.setWidth(100)  # Adjust the width of the rectangle cursor
        self.setCursorWidth(10)  # Set cursor width to match the rectangle    
        # Timer for blinking effect
        self.blink_timer = QTimer(self)
        self.blink_timer.timeout.connect(self.toggle_cursor)
        self.blink_timer.start(500)  # Blink interval in milliseconds
        # Initial state
        self.cursor_visible = True
    def toggle_cursor(self):
        # Toggle cursor visibility
        self.cursor_visible = not self.cursor_visible
    def paintEvent(self, event):
        # Custom paint event to draw the cursor as a rectangle
        super().paintEvent(event)    
        if not self.textCursor().hasSelection() and self.cursor_visible and self.hasFocus():
            cursor = self.textCursor()
            cursor_pos = self.cursorRect(cursor)
            # Get foreground color from palette
            color = self.palette().color(QPalette.Text)
            # Draw the rectangle cursor
            painter = QPainter(self.viewport())
            painter.fillRect(cursor_pos, color)
    def setWorkingdirectory(self, path):
        self.strd = path
    def startShell(self):
        if sys.platform == "win32":
           self.systemname = "powershell"
           self.process.start("powershell.exe", ["-NoLogo", "-NoExit"])
        # else:
        #        self.process.start("powershell.exe", ["-NoLogo", "-NoExit","-WorkingDirectory", self.strd])
        else:
            self.process.start("bash")
            self.systemname = "bash"
    def clear_Terminal(self):
        self.clear()
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.executeCommand()
        elif event.key() == Qt.Key_Backspace:
            if self.textCursor().positionInBlock() > self.command_start_position:
                super().keyPressEvent(event)
        elif event.key() == Qt.Key_Up:
            self.navigateHistory(-1)
        elif event.key() == Qt.Key_Down:
            self.navigateHistory(1)
        else:
            super().keyPressEvent(event)
    def executeCommand(self):
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)
        # Extract the command entered by the user
        current_text = self.toPlainText()
        command = current_text[self.command_start_position:].strip()
        if self.check_if_special_command(command):
            self.execute_special_command(command)
            self.commandHistory.append(command)
            self.historyIndex = len(self.commandHistory)
            self.append("")
            return
        if command:
            self.commandHistory.append(command)
            self.historyIndex = len(self.commandHistory)
            full_command = command + "\n"  # Add newline to simulate Enter press
            self.process.write(full_command.encode())
            self.append("")  # Move to the next line
            processname = full_command.strip(" ")[0]
        else:
            self.append(self.prompt)  # move to the next line
    def navigateHistory(self, direction):
        if self.commandHistory:
            self.historyIndex = (self.historyIndex + direction) % len(self.commandHistory)
            self.replaceCommand(self.commandHistory[self.historyIndex])
    def readOutput(self):
        output = self.process.readAll().data().decode(errors='ignore')
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)
        self.insertPlainText(output)
        # Extract the new prompt
        self.prompt = output.splitlines()[-1] if output.splitlines() else ""
        self.command_start_position = self.textCursor().position()
    def replaceCommand(self, command):
        cursor = self.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        cursor.removeSelectedText()
        cursor.insertText(self.prompt + command)
        self.setTextCursor(cursor)
    def check_if_special_command(self,command):
        new = command.split(" ")
        if new[0] == "code":
            return True
        else: return False
    def execute_special_command(self,command):
        new = command.split(" ")
        if new[0] == "code":
            self.main_window.code_command(new[1])
        else: return
            

class TerminalManager(QWidget):
    def __init__(self,main_window):
        super(TerminalManager, self).__init__()
        
        self.main_layout = QHBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_window = main_window
        # Sidebar layout on the left side
        self.sidebar_layout = QVBoxLayout()

        # Sidebar for terminal list
        self.sidebar = QListWidget()
        self.sidebar.setObjectName("TerminalList")
        self.sidebar.setFixedWidth(150)
        self.sidebar.currentRowChanged.connect(self.switch_terminal)
        heading = Heading(self)
        heading.setFixedHeight(45)  # Ensure the heading has a fixed height
        self.sidebar_layout.addWidget(heading)
        self.sidebar_layout.addWidget(self.sidebar)

        # Add/Delete buttons under the list
      # Add the heading to the sidebar layout

        # Terminal stack layout
        self.terminal_stack = QStackedWidget()
        self.main_layout.addWidget(self.terminal_stack)

        # Stretch to push sidebar to the left
        self.sidebar_layout.addStretch()

        # Add sidebar layout to the main layout
        self.main_layout.addLayout(self.sidebar_layout)


        # Counter for terminals
        self.terminal_count = 0
    def add_Terminal(self):
        # Create a new terminal instance
        self.terminal = TerminalWidget(self.main_window)  # Assuming TerminalWidget is defined elsewhere
        # Add the terminal to the stacked widget
        terminal_index = self.terminal_stack.addWidget(self.terminal)
        # Create a list item in the sidebar
        terminal_name = self.terminal.systemname
        self.terminal_count += 1
        list_item = QListWidgetItem(terminal_name)
        list_item.setData(Qt.UserRole, terminal_index)
        self.sidebar.addItem(list_item)
        self.sidebar.setCurrentItem(list_item)

    def delete_Terminal(self):
        # Get the current terminal index
        current_index = self.sidebar.currentRow()
        if current_index >= 0:
            # Remove the widget from stacked widget and sidebar
            widget = self.terminal_stack.widget(current_index)
            self.terminal_stack.removeWidget(widget)
            widget.deleteLater()
            self.sidebar.takeItem(current_index)

    def switch_terminal(self, index):
        # Switch the terminal in the stacked widget
        self.terminal_stack.setCurrentIndex(index)

    # Existing code to hide terminal frame if needed
    def hide_terminal_frame(self):
        if hasattr(self, 'terminal_frame_on') and self.terminal_frame_on:
            self.terminal_frame.hide()