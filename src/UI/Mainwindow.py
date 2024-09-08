from PyQt5.QtWidgets import (
    QFrame,
    QSizePolicy,
    QHBoxLayout,
    QSplitter,
    QVBoxLayout,
    QTabWidget,
    QLineEdit, QCheckBox, QLabel,
    QListWidget,
    QSpacerItem,
    QMessageBox,QFileDialog
)
from Filesystem.file_types import FileType, get_file_type,get_current_lang
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QEnterEvent, QMouseEvent
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QIcon
from Editor.editor_h import Editor
from Filesystem.file_manager import FileManager
from Filesystem.fuzzy_searcher import SearchItem, SearchWorker
from UI.heading import Heading
from qframelesswindow import FramelessMainWindow
import sys
import os
from pathlib import Path
import jedi
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
   QFrame, QHBoxLayout, QLabel,QPushButton
)
from UI.UImanager import init_ui
from lib.QCodeTerminal import TerminalManager
from Editor.shortcuts import LoadShortcuts
from UI.log import LogSystem
from Settings.datapaths import ICON_PATH, FILEI_PATH
from Frames.basewidgets import *
from Settings.settings import WINDOW_FONT
from lib.AlertWidget import AlertWidget
from AI.ollamamanager import OllamaManager
class MainWindow(FramelessMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app_name = "Minsky"
        self.app = app
        self.current_file = None
        self.file_open = False
        self.current_side_bar = None
        self.envs = list(jedi.find_virtualenvs())
        self.file_type = None
        self.current_files = {}
        self.current_indexes = {}
         #Currently opened Windows:
        self.editor_closed = False
        self.language_frame_open = False
        self.file_m_open = False
        self.log_frame_on = False
        self.welcome_frame_on = True
        self.first_tab_on = False
        self.welcome_frame_index = None
        self.terminal_first_launch = False
        self.current_dir = os.getcwd()
        init_ui(self)
        self.ollama = OllamaManager(self)
        self.ollama.setup()
    @property
    def current_file(self) -> Path:
        return self._current_file
    @current_file.setter
    def current_file(self, file: Path):
        self._current_file: Path = file
    def get_editor(self,filetype, path: Path = None) -> QsciScintilla:
        venv = None
        if len(self.envs) > 0:
            venv = self.envs[0]
        editor = Editor(self,file_type=filetype, path=path, env=venv)
        #self.lang_name = editor.lang_name
        return editor
    def set_cursor_pointer(self, e: QEnterEvent) -> None:
        self.setCursor(Qt.PointingHandCursor)
    def set_cursor_arrow(self, e) -> None:
        self.setCursor(Qt.ArrowCursor)
    def get_sidebar_button(self, img_path: str, widget) -> QLabel:
        label = QLabel()
        label.setStyleSheet("border: none; padding: 4px;")
        icon = QIcon(img_path)
        label.setPixmap(icon.pixmap(30, 30))
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        label.setFont(self.window_font)
        label.mousePressEvent = lambda e: self.show_hide_tab(e, widget)
        label.setMouseTracking(True)
        label.enterEvent = self.set_cursor_pointer
        label.leaveEvent = self.set_cursor_arrow
        return label
    def Language_Frame(self, language):
        if self.language_frame_open:
            pass
        else:
            self.lang_Frame = get_frame()
            self.lang_Frame.setObjectName("MinskyLanguageFrame")
            lang_layout = QVBoxLayout()
            lang_layout.setContentsMargins(0, 0, 0, 0)
            lang_layout.setSpacing(20)
            lang_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            wlcm_title = self.create_label(
                "C++",
                "color: #8246fa;",
                Qt.AlignmentFlag.AlignAbsolute,
                font_size=40,
                min_height=90,
            
            )
            wlcm_msg = create_label(
                "Something about the language",
                "color: #8246fa;",
                Qt.AlignmentFlag.AlignTop,
                font_size=15,
                min_height=100,
            )  
            button = QPushButton("Close", self.lang_Frame)
            button.clicked.connect(self.frameclose)
            self.lang_Frame.setLayout(lang_layout)
            self.lang_Frame.setStyleSheet(self.lang_Frame.styleSheet() + "border: none;")
            lang_layout.addWidget(wlcm_title)
            lang_layout.addWidget(wlcm_msg)
            self.hsplit.addWidget(self.lang_Frame)
            idx = self.hsplit.indexOf(self.lang_Frame)
            if idx != -1:
                self.hsplit.replaceWidget(idx, self.tab_view)
                self.tab_view.close()
                self.editor_closed = True
                self.language_frame_open = True
    def setUpBody(self):   
        body_frame = QFrame()
        body_frame.setFrameShape(QFrame.NoFrame)
        body_frame.setFrameShadow(QFrame.Plain)
        body_frame.setLineWidth(0)
        body_frame.setMidLineWidth(0)
        body_frame.setContentsMargins(0, 0, 0, 0)
        body_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)
        self.hsplit = QSplitter(Qt.Horizontal)
        self.vsplit = QSplitter(Qt.Vertical)
        self.tab_view = QTabWidget()
        self.tab_view.setContentsMargins(0, 0, 0, 0)
        self.tab_view.setTabsClosable(True)
        self.tab_view.setMovable(True)
        self.tab_view.setDocumentMode(True)
        self.tab_view.tabCloseRequested.connect(self.close_tab)
        self.tab_view.setMouseTracking(True)
        self.tab_view.enterEvent = self.set_cursor_pointer
        self.tab_view.leaveEvent = self.set_cursor_arrow
        self.tab_view.currentChanged.connect(self.tab_changed)
        self.tab_view.setFont(QFont(self.window_font))
        self.tab_view.setTabBarAutoHide(True)
        self.tab_view.tabBar().installEventFilter(self.tab_view)
        self.side_bar = QFrame()
        #File  Manager
        self.file_manager_frame = get_frame()
        self.file_manager_frame.setMaximumWidth(400)
        self.file_manager_frame.setMinimumWidth(200)
        self.file_manager_layout = QVBoxLayout() 
        self.file_manager_layout.setContentsMargins(0, 0, 0, 0)
        self.file_manager_layout.setSpacing(0)
        label_text = self.splitted_dir(str(Path(os.getcwd())))
        #self.current_dir_lbl = QLabel(label_text)
        #self.current_dir_lbl.setObjectName("CurrentDir")
        self.file_manager = FileManager(tab_view=self.tab_view,set_new_tab=self.set_new_tab, main_window=self) 
        #self.file_manager_layout.addWidget(self.current_dir_lbl)
        self.file_manager_layout.addWidget(self.file_manager)
        self.file_manager_frame.setLayout(self.file_manager_layout)
        if self.file_m_open: self.file_manager_frame.show()
        else: self.file_manager_frame.hide()
      #Extensions ------- Frame
        self.extension_frame = get_frame()
        self.extension_frame.setMaximumWidth(400)
        self.extension_frame.setMinimumWidth(200)
        extension_layout = QVBoxLayout()
        extension_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        extension_layout.setContentsMargins(0, 10, 0, 0)
        extension_layout.setSpacing(0)
        extension_input = QLineEdit()
        extension_input.setPlaceholderText("Search for Extension")
        extension_input.setFont(self.window_font)
        extension_input.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.extension_frame.setLayout(extension_layout)
      #Search -------- Frame
        self.search_frame = get_frame()
        self.search_frame.setMaximumWidth(400)
        self.search_frame.setMinimumWidth(200)
        search_layout = QVBoxLayout()
        search_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        search_layout.setContentsMargins(0, 10, 0, 0)
        search_layout.setSpacing(0)
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search")
        search_input.setFont(self.window_font)
        search_input.setAlignment(Qt.AlignmentFlag.AlignTop)
        ############# CHECKBOX ################
        self.search_checkbox = QCheckBox("Search in modules")
        self.search_checkbox.setFont(self.window_font)
        self.search_checkbox.setStyleSheet("color: white; margin-bottom: 10px;")
        self.search_worker = SearchWorker()
        self.search_worker.finished.connect(self.search_finished)
        search_input.textChanged.connect(
            lambda text: self.search_worker.update(
                text,
                self.file_manager.model.rootDirectory().absolutePath(),
                self.search_checkbox.isChecked(),
            )
        )
        ############## Search ListView ####################
        self.search_list_view = QListWidget()
        self.search_list_view.setFont(QFont("FiraCode", 13))
        self.search_list_view.itemClicked.connect(self.search_list_view_clicked)
        search_layout.addWidget(self.search_checkbox)
        search_layout.addWidget(search_input)
        search_layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum))
        search_layout.addWidget(self.search_list_view)
        self.search_frame.setLayout(search_layout)
        self.WelcomeFrame()
        self.Deltasphere_ai_frame()  
        self.file_manager_frame.setStyleSheet(self.file_manager_frame.styleSheet() + "border: none;")
        self.side_bar.setStyleSheet(self.side_bar.styleSheet() + "border: none; border-right: 1px solid #333641;")
        self.tab_view.setStyleSheet(self.tab_view.styleSheet() + "border: none;")
        self.hsplit.setStyleSheet(self.hsplit.styleSheet() + "border: none;")
        body_frame.setStyleSheet(body_frame.styleSheet() + "border: none;")
        self.hsplit.addWidget(self.file_manager_frame)
        self.hsplit.addWidget(self.welcome_frame)
        self.add_Terminal(body,body_frame)
        self.vsplit.addWidget(self.terminal_frame)
        self.current_side_bar = None
        self.header = Heading(self)
        self.header.setStyleSheet(self.header.styleSheet() + "border: none; border-bottom-left-radius: 0; border-bottom-right-radius: 0;")
        full_body = QVBoxLayout()
        full_body.setContentsMargins(0, 0, 0, 0)
        full_body.setSpacing(0)
        full_body.addWidget(self.header)
        full_body.addLayout(body)
        body_frame.setLayout(full_body)
        body.addWidget(self.hsplit)
        self.vsplit.addWidget(body_frame)
        self.addlogframe(body,body_frame)      
        self.setCentralWidget(body_frame)
        body_frame.setObjectName("MinskyCentralWidget")  
        #Shortcuts
        LoadShortcuts(self)    
    def splitted_dir(self,dir: str):
        dummy_dir = dir.split('\\')
        dummy_str = ""
        for word in dummy_dir:
            if word == dummy_dir[-1]:
                dummy_str = dummy_str + word
            else:
                dummy_str = dummy_str + word + " > "
        if len(dummy_str) >= 50:
            dummy_str = dummy_str[:51] + "..."
        return dummy_str
    def add_Terminal(self, body, body_frame,):
        self.terminal = TerminalManager(self)
        self.terminal_frame_on = True
        if self.current_file == None:
            pass
        else:
            self.terminal.setWorkingdirectory(self.current_file)
        self.terminal_frame = QFrame()
        self.terminal_frame.setFrameShape(QFrame.NoFrame)
        self.terminal_frame.setFrameShadow(QFrame.Plain)
        self.terminal_frame.setLineWidth(0)
        self.terminal_frame.setMidLineWidth(0)
        self.terminal_frame.setContentsMargins(0, 0, 0, 0)
        self.terminal_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        terminal_layout = QVBoxLayout()
        terminal_layout.setContentsMargins(0, 0, 0, 0)
        terminal_layout.setSpacing(0)
        terminal_layout.addWidget(self.terminal)
        if self.terminal_first_launch == False:
            self.terminal.add_Terminal()
        self.terminal_frame.setLayout(terminal_layout)
        self.terminal_frame.hide()
    def addlogframe(self, body, body_frame):
        self.logsys = LogSystem()
        self.log_frame_on = True
        full_body = QVBoxLayout()
        full_body.setContentsMargins(0, 0, 0, 0)
        full_body.setSpacing(0)
        full_body.addLayout(body)
        self.log_frame = QFrame()
        self.log_frame.setFrameShape(QFrame.NoFrame)
        self.log_frame.setFrameShadow(QFrame.Plain)
        self.log_frame.setLineWidth(0)
        self.log_frame.setMidLineWidth(0)
        self.log_frame.setContentsMargins(0, 0, 0, 0)
        self.log_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        log_layout = QVBoxLayout()
        log_layout.setContentsMargins(0, 0, 0, 0)
        log_layout.setSpacing(0)
        log_layout.addWidget(self.logsys)
        self.log_frame.setLayout(log_layout)
        full_body.addWidget(self.log_frame)
        body_frame.setLayout(full_body)
        self.log_frame.hide()
        self.Alertwidget = AlertWidget()     
    def maximizetab(self):
        self.showMaximized()
    def search_finished(self, items):
        self.search_list_view.clear()
        for i in items:
            self.search_list_view.addItem(i)
    def search_list_view_clicked(self, item: SearchItem):
        self.set_new_tab(Path(item.full_path))
        editor: Editor = self.tab_view.currentWidget()
        editor.setCursorPosition(item.lineno, item.end)
        editor.setFocus()
    def show_hide_tab(self, e: QMouseEvent, widget: str):
      
        if self.current_side_bar == widget:
            if widget.isHidden():
                widget.show()
            else:
                widget.hide()

            return
       
        self.hsplit.replaceWidget(0, widget)
        self.current_side_bar = widget
        self.current_side_bar.show()
    def show_dialog(self, title, msg) -> int:
        dialog = QMessageBox(self)
        dialog.setFont(self.font())
        dialog.font().setPointSize(14)
        dialog.setWindowTitle(title)
        dialog.setWindowIcon(QIcon(ICON_PATH +"close_icon.png"))
        dialog.setText(msg)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        dialog.setIcon(QMessageBox.Warning)
        return dialog.exec_()
    def close_tab(self, index: int):    
        editor: Editor = self.tab_view.currentWidget()
        if editor.current_file_changed:
            dialog = self.show_dialog(
                "Close", f"Do you want to save the changes made to {self.current_file.name}?"
            )
            if dialog == QMessageBox.Yes:
                self.save_file()
        self.tab_view.removeTab(index)

    def tab_changed(self, index: int):  
        editor = self.tab_view.widget(index)
        if editor:
             self.current_file = editor.path
    def frameclose(self):
        if self.editor_closed:
            self.tab_view.show()
            self.lang_Frame.close()
            self.language_frame_open = False
            self.editor_closed = False
        else:
            pass        
    def is_binary(self, path):
        """
        Check if file is binary
        """
        with open(path, "rb") as f:
            return b"\0" in f.read(1024)
    def copy(self):
        t = self.tab_view.currentWidget()
        if t is not None:
            t.copy()  
    def set_new_tab(self, path: Path, is_new_file=False):
        if not is_new_file and self.is_binary(path):
            self.statusBar().showMessage("Cannot Open Binary File", 2000)
            return        
        if path.is_dir():
            return        
        if self.welcome_frame:
            idx = self.hsplit.indexOf(self.welcome_frame)
            if idx != -1:
                self.hsplit.replaceWidget(idx, self.tab_view)
                self.welcome_frame_on = False
        if is_new_file:
            text_edit = self.get_editor(path, path.suffix)
            self.tab_view.addTab(text_edit, "untitled")
            self.setWindowTitle("untitled - " + self.app_name)
            self.statusBar().showMessage(f"Opened untitled", 2000)
            self.tab_view.setCurrentIndex(self.tab_view.count() - 1)            
            self.current_file = None
            self.first_tab_on = True
            return     
        for i in range(self.tab_view.count()):           
            if self.tab_view.tabText(i) == path.name or self.tab_view.tabText(i) == "*"+path.name:               
                self.tab_view.setCurrentIndex(i)
                self.current_file = path                
                return
        w_s = path.name.removesuffix(path.suffix)
        current_dir =os.path.dirname(os.path.realpath(__file__))
        file_type: FileType = get_file_type(path.suffix)
        text_edit = self.get_editor(get_file_type(path.suffix),path)
        self.current_files[path] = text_edit
        self.current_indexes[path] = self.tab_view.count()
        self.file_open = True
        self.first_tab_on = True
        tab_icon = None
        if file_type != FileType.Other:
                try:
                    tab_icon = QIcon(FILEI_PATH+f"{get_current_lang(file_type)}.svg")
                except FileNotFoundError:
                    pass 
        else:
                try:
                    tab_icon = QIcon(ICON_PATH+"file.svg")
                except FileNotFoundError:
                    pass
        
        self.tab_view.addTab(text_edit,tab_icon, path.name)
        text_edit.setText(path.read_text(encoding="utf-8"))
        self.setWindowTitle(f"{path.name} - {self.app_name}")
        self.statusBar().showMessage(f"Opened {path.name}", 2000)  
        self.tab_view.setCurrentIndex(self.tab_view.count() - 1)
        self.current_file = path
        self.logsys.addLog(f"Current File: {self.current_file} | Type : {self.file_type}",self.logsys.validFormat)
        self.logsys.addLog(f"Current Files: {self.current_files} |Length: {len(self.current_files)}",self.logsys.validFormat)
    def new_file(self):       
        self.set_new_tab(Path("Untitled File"), True)
    def save_file(self):      
        if self.current_file is None and self.tab_view.count() > 0:
            self.save_as()
            return
        if self.current_file is None:
            return
        text_edit = self.tab_view.currentWidget()
        self.current_file.write_text(text_edit.text())
        self.statusBar().showMessage(f"Saved {self.current_file.name}", 2000)
        self.logsys.addLog(f"Saved: {self.current_file.name}",self.logsys.validFormat)    
        text_edit.current_file_changed = False
    def save_as(self):       
        text_edit = self.tab_view.currentWidget()
        if text_edit is None:
            return
        file_path = QFileDialog.getSaveFileName(self, "Save As", os.getcwd())[0]
        if file_path == "":
            self.statusBar().showMessage("Cancelled", 2000)
            return
        path = Path(file_path)
        path.write_text(text_edit.text())
        self.current_file = path
        self.tab_view.setTabText(self.tab_view.currentIndex(), path.name)
        self.statusBar().showMessage(f"Saved {path.name}", 2000)       
        editor: Editor = self.tab_view.currentWidget()
        editor.current_file_changed = False
    def open_file_dlg(self):
        new_file, _ = QFileDialog.getOpenFileName(
            self, "Pick A File", "", "All Files (*);;Python Files (*.py)"
        )
        if new_file:
            f = Path(new_file)
            self.set_new_tab(f)
    def open_folder(self):
        new_folder = QFileDialog.getExistingDirectory(
            self, "Pick A Folder", "")
        if new_folder:
            self.file_manager.model.setRootPath(new_folder)
            self.file_manager.setRootIndex(self.file_manager.model.index(new_folder))
            self.statusBar().showMessage(f"Opened {new_folder}", 2000)
            #self.current_dir_lbl.setText(Path(new_folder).name)
            #self.current_dir = Path(new_folder)
            self.tab_view.clear()
            idx = self.hsplit.indexOf(self.tab_view)
            if idx != -1:
                self.hsplit.replaceWidget(idx, self.welcome_frame)
    def save_all(self):
        n = 0
        self.Alertwidget.show_message('Saving All...',2000)
        for file in self.current_files:
            if os.path.isdir(file):
                editor = self.current_files[file]
                file.write_text(editor.text())
                n += 1
        self.logsys.addLog(f"Saved All ({n} Files in total)",self.logsys.actionFormat)
        self.statusBar().showMessage(f"Saved All", 2000)
    def WelcomeFrame(self):
        self.welcome_frame = get_frame()
        self.welcome_frame.setObjectName("WelcomeFrame")
        welcome_layout = QVBoxLayout()
        welcome_layout.setContentsMargins(0, 0, 0, 0)
        welcome_layout.setSpacing(20)
        welcome_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        wlcm_title = create_label(
            "Minsky",
            "color: #8246fa;",
            Qt.AlignmentFlag.AlignHCenter,
            font_size=25,
            min_height=90,
            
        )
        wlcm_msg = create_label(
            "Crafting Code, Creating Future.\n  Lukas Rennhofer @2024  ",
            "color: #8246fa;",
            Qt.AlignmentFlag.AlignHCenter,
            font_size=15,
            min_height=100,
        )
        wlcm_start_now_b = QPushButton(self.welcome_frame, text="Version 0.0.1")
        wlcm_start_now_b.setObjectName("wlcmbutton1")
        wlcm_title.setFont(QFont("Blanka",50))
        welcome_layout.addWidget(wlcm_title)
        welcome_layout.addWidget(wlcm_msg)
        welcome_layout.addWidget(wlcm_start_now_b)
        self.welcome_frame.setLayout(welcome_layout)
        self.welcome_frame.setStyleSheet(self.welcome_frame.styleSheet() + "border: none;")
    def Deltasphere_ai_frame(self):
        self.Deltasphere_Frame = get_frame()

        # Layout for the AI frame
        ai_layout = QVBoxLayout()
        ai_layout.setContentsMargins(10, 10, 10, 10)
        ai_layout.setSpacing(15)
        ai_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Input label
        input_label = create_label(
            "",
            "color: #38b6ff;",  # Text color for the input label
            Qt.AlignmentFlag.AlignHCenter,
            font_size=16
        )

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setObjectName("AIInputField")
        self.input_field.setStyleSheet("background-color: #001f33; color: #ffffff; border: 1px solid #004080; border-radius: 4px; padding: 5px;")
        self.input_field.setPlaceholderText("Type your query here...")
        self.input_field.setFixedWidth(400)
        input_label.setFont(QFont("Blanka", 50))
        # Send button
        self.send_button = QPushButton("Create")
        self.send_button.setObjectName("AISendButton")
        self.send_button.setStyleSheet("background-color: #8246fa; color: #ffffff;width: 100px; border: none; border-radius: 5px; padding: 10px; font-size: 16px;")
        self.send_button.setFixedWidth(200)
        
        wlcm_start_now_b = QPushButton(self.welcome_frame, text="See Activities")
        wlcm_start_now_b.setObjectName("wlcmbutton1")
        # Add widgets to layout
        ai_layout.addWidget(input_label)
        ai_layout.addWidget(self.input_field)
        ai_layout.addWidget(self.send_button, alignment=Qt.AlignmentFlag.AlignCenter)
        ai_layout.addWidget(wlcm_start_now_b)

        # Apply layout to frame
        self.Deltasphere_Frame.setLayout(ai_layout)
        self.Deltasphere_Frame.setStyleSheet(self.Deltasphere_Frame.styleSheet() + "border: none;")  # Ensure no border
            
    def code_command(self,file_name):
        dirc = self.current_dir
        file_path = Path(os.path.join(dirc, file_name))
        with open(file_path, 'w') as file: pass
        self.set_new_tab(file_path)
            

    
