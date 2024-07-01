from PyQt5.QtWidgets import (
    QApplication,
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


class MainWindow(FramelessMainWindow):
    def __init__(self):
        super().__init__()
        self.app_name = "Minsky"

        self.current_file = None
        self.current_side_bar = None
        self.envs = list(jedi.find_virtualenvs())
        self.file_type = None
        init_ui(self)
        #Current opened Windows:
        self.editor_closed = False
        self.language_frame_open = False
        

    @property
    def current_file(self) -> Path:
        return self._current_file

    @current_file.setter
    def current_file(self, file: Path):
        self._current_file: Path = file
    def ofs(self,path) -> str:
        return os.getcwd() + "/src/UI" + path
    def get_editor(self, path: Path = None, file_type="Other") -> QsciScintilla:
       
        venv = None
        if len(self.envs) > 0:
            venv = self.envs[0]
       
        editor = Editor(self, path=path, env=venv, file_type=file_type)
        self.lang_name = editor.lang_name
        
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

    def get_frame(self) -> QFrame:
        frame = QFrame()
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Plain)
        frame.setContentsMargins(1, 1, 1, 1)
        frame.setStyleSheet(
        """
            QFrame {
                background-color: #21252b;
                border-radius: 5px;
                border: none;
                padding: 5px;
                color: #D3D3D3;
                float: left;
            }

            QFrame::hover {
                color: white;
            }
        """
        )

        return frame

    def create_label(self, text, style_sheet, alignment, font="Consolas", font_size=15, min_height=200):
        lbl = QLabel(text)
        lbl.setAlignment(alignment)
        lbl.setFont(QFont(font, font_size))
        lbl.setStyleSheet(style_sheet)
        lbl.setContentsMargins(0, 0, 0, 0)
        lbl.setMaximumHeight(min_height)
        return lbl
    def Language_Frame(self, language):
        if self.language_frame_open:
            pass
        else:
            self.lang_Frame = self.get_frame()
            self.lang_Frame.setStyleSheet(
            """
                QFrame {
                    background-color: #21252b;
                    border: none;
                    color: #D3D3D3;
                }
                QFrame::hover {
                    color: white;
                }
            """
            )

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
            wlcm_msg = self.create_label(
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
        self.tab_view.setFont(QFont("Zed Mono Extended"))
        self.tab_view.setTabBarAutoHide(True)
        self.side_bar = QFrame()

        
        

      
        self.file_manager_frame = self.get_frame()
        self.file_manager_frame.setMaximumWidth(400)
        self.file_manager_frame.setMinimumWidth(200)

        
        
        self.file_manager_layout = QVBoxLayout() 
        self.file_manager_layout.setContentsMargins(0, 0, 0, 0)
        self.file_manager_layout.setSpacing(0)


      
        self.current_dir_lbl = QLabel(Path(os.getcwd()).name)
        self.current_dir_lbl.setStyleSheet("""
        font-size: 14px;
        background-color: #282c34;
        font-weight: bold;
        """)

        self.file_manager = FileManager(tab_view=self.tab_view,set_new_tab=self.set_new_tab, main_window=self) 
        
        self.file_manager_layout.addWidget(self.current_dir_lbl)
        self.file_manager_layout.addWidget(self.file_manager)
        self.file_manager_frame.setLayout(self.file_manager_layout)
      #Extensions ------- Frame
        self.extension_frame = self.get_frame()
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
        self.search_frame = self.get_frame()
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

        ###############################################
        ############## Search ListView ####################
        self.search_list_view = QListWidget()
        self.search_list_view.setFont(QFont("FiraCode", 13))

        self.search_list_view.itemClicked.connect(self.search_list_view_clicked)

        search_layout.addWidget(self.search_checkbox)
        search_layout.addWidget(search_input)
        search_layout.addSpacerItem(
            QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)
        )
        search_layout.addWidget(self.search_list_view)
        self.search_frame.setLayout(search_layout)

        

        # labelw = self.get_sidebar_button(os.path.join(sys.path[0], "UI/icons/folder_icon.svg"), self.file_manager_frame)
        # side_bar_content.addWidget(labelw)

        # #side_button_content_widget("./UI/folder_icon.svg", self.file_manager_frame)
        # search_label = self.get_sidebar_button(os.path.join(sys.path[0], "UI/icons/search_icon.svg"), self.search_frame)
        # side_bar_content.addWidget(search_label)
        # plugin_label = self.get_sidebar_button(os.path.join(sys.path[0], "UI/icons/extension_1.svg"), self.extension_frame)
        # side_bar_content.addWidget(plugin_label)
        # copilot_label = self.get_sidebar_button(os.path.join(sys.path[0], "UI/icons/copilot.svg"), self.extension_frame)
        # side_bar_content.addWidget(copilot_label)

        # delete not !
        #self.side_bar.setLayout(side_bar_content)
        #body.addWidget(self.side_bar)
        #----
     
        self.welcome_frame = self.get_frame()
        self.welcome_frame.setStyleSheet(
        """
            QFrame {
                background-color: #21252b;
                border: none;
                color: #D3D3D3;
            }
            QFrame::hover {
                color: white;
            }
        """
        )

        welcome_layout = QVBoxLayout()
        welcome_layout.setContentsMargins(0, 0, 0, 0)
        welcome_layout.setSpacing(20)
        welcome_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        wlcm_title = self.create_label(
            "Welcome to Minsky!",
            "color: #8246fa;",
            Qt.AlignmentFlag.AlignHCenter,
            font_size=25,
            min_height=90,
            
        )
        wlcm_msg = self.create_label(
            "Crafting Code, Creating Future.\n - LRDev @2024 - ",
            "color: #8246fa;",
            Qt.AlignmentFlag.AlignHCenter,
            font_size=15,
            min_height=100,
        )
        wlcm_start_now_b = QPushButton(self.welcome_frame, text="")
        wlcm_start_now_b.setObjectName("wlcmbutton1")
        welcome_layout.addWidget(wlcm_title)
        welcome_layout.addWidget(wlcm_msg)
        welcome_layout.addWidget(wlcm_start_now_b)
        self.welcome_frame.setLayout(welcome_layout)

        self.file_manager_frame.setStyleSheet(self.file_manager_frame.styleSheet() + "border: none;")
        self.welcome_frame.setStyleSheet(self.welcome_frame.styleSheet() + "border: none;")
        self.side_bar.setStyleSheet(self.side_bar.styleSheet() + "border: none; border-right: 1px solid #333641;")
        self.tab_view.setStyleSheet(self.tab_view.styleSheet() + "border: none;")
        self.hsplit.setStyleSheet(self.hsplit.styleSheet() + "border: none;")
        
        body_frame.setStyleSheet(body_frame.styleSheet() + "border: none;")

        
       
        self.hsplit.addWidget(self.file_manager_frame)
        self.hsplit.addWidget(self.welcome_frame)
        self.current_side_bar = None

      
        self.header = Heading(self)
        self.header.setStyleSheet(self.header.styleSheet() + "border: none; border-bottom: 1px solid #333641; border-bottom-left-radius: 0; border-bottom-right-radius: 0;")

        body.addWidget(self.hsplit)

      
        full_body = QVBoxLayout()
        full_body.setContentsMargins(0, 0, 0, 0)  
        full_body.setSpacing(0)
        full_body.addWidget(self.header)        
        full_body.addLayout(body)        

        body_frame.setLayout(full_body)
       

        self.setCentralWidget(body_frame)
        self.frame_stlye = f"""
        QFrame {{
            background: #282c34;
            border-radius: 10px;
            border: 0.5px solid #3A3E49;
            border-bottom-left-radius: 0; 
            border-bottom-right-radius: 0;
        }}
        """
        self.frame_style_no_border = f"""
        QFrame {{
            background: #282c34;
            border-radius: 0px;
        }}
        """
        
        self.centralWidget().setStyleSheet(self.frame_stlye)
    
        
        
        
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
        dialog.setWindowIcon(QIcon(os.path.join(sys.path[0], "UI/icons/close_icon.png")))
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

        text_edit = self.get_editor(path, path.suffix)
        
        if is_new_file:
            self.tab_view.addTab(text_edit, "untitled")
            self.setWindowTitle("untitled - " + self.app_name)
            self.statusBar().showMessage(f"Opened untitled", 2000)
            self.tab_view.setCurrentIndex(self.tab_view.count() - 1)
            
            self.current_file = None
            return

      
        for i in range(self.tab_view.count()):
           
            if self.tab_view.tabText(i) == path.name or self.tab_view.tabText(i) == "*"+path.name:
               
                self.tab_view.setCurrentIndex(i)
                self.current_file = path
                
                return

        self.tab_view.addTab(text_edit, path.name)
        text_edit.setText(path.read_text(encoding="utf-8"))
        self.setWindowTitle(f"{path.name} - {self.app_name}")
        self.statusBar().showMessage(f"Opened {path.name}", 2000)
        
        self.tab_view.setCurrentIndex(self.tab_view.count() - 1)
        self.current_file = path
        print(self.current_file)


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
       
        text_edit.current_file_changed = False
    def save_all(self):
        pass

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
        # new
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
            self, "Pick A Folder", ""
        )
        if new_folder:
            self.file_manager.model.setRootPath(new_folder)
            self.file_manager.setRootIndex(self.file_manager.model.index(new_folder))
            self.statusBar().showMessage(f"Opened {new_folder}", 2000)
            self.current_dir_lbl.setText(Path(new_folder).name)

            self.tab_view.clear()
            idx = self.hsplit.indexOf(self.tab_view)
            if idx != -1:
                self.hsplit.replaceWidget(idx, self.welcome_frame)

    
