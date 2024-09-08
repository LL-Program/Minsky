from typing import TYPE_CHECKING

from pathlib import Path
from PyQt5.Qsci import QsciScintilla, QsciAPIs
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont, QColor, QKeyEvent,QImage
from UI.debug import *
from Lexer.lexer import JsonLexer
from Lexer.PyLexer import PyCustomLexer, PyAutoCompleter
from Lexer.CppLexer import CppCustomLexer
from Lexer.CLexer import CCustomLexer
from Filesystem.file_types import get_file_type,searchfiletype, FileType, get_current_lang
from Editor.autocompleter import AutoCompleter
import sys
if TYPE_CHECKING:
    from UI.Mainwindow import MainWindow
from Settings.settings import EDITOR_FONT
from Settings.StyleManager import load_theme, current_theme
from Settings.datapaths import STYLES_PATH
from UI.defaultassets import * 
class Editor(QsciScintilla):
    def __init__(self, main_window,file_type, parent=None, path: Path = None, env=None):
        super(Editor, self).__init__(parent)
        self.first_launch = True 
        self.main_window: MainWindow = main_window
        self.file_open = main_window.file_open
        self.is_auto_file = False
        self.path = path
        self.file_type = file_type
        self.lang_name =  get_current_lang(self.file_type)
        main_window.file_type = self.file_type
        self.is_python_file = self.file_type == FileType.Python
        self.full_path = self.path.absolute()
        self.current_button_line = None
        self.venv = env
        self._current_file_changed = False
        self.cursorPositionChanged.connect(self.cursorPositionChangedCustom)
        self.textChanged.connect(self.textChangedCustom)   
        self.setUtf8(True)
        self.font = QFont(EDITOR_FONT, 12)
        self.setFont(self.font)
        #log-sys----
        self.logsys_on = False
        #for online Server
        self.setObjectName("Editor")
        self.linesnumber = self.lines()
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setTabWidth(4)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False) 
        self.setAutoIndent(True)
        indent_guide_color = QColor('#ffffff')  # Dark gray color (or choose any color you prefer)
        self.setIndentationGuidesForegroundColor(indent_guide_color)
        self.setIndentationGuidesBackgroundColor(indent_guide_color)
        self.marker_sysmbol1 = self.MarkerSymbol.Circle
        self.markerDefine(self.marker_sysmbol1, 0)
        self.setAutoCompletionSource(QsciScintilla.AcsAPIs)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)
        self.setCallTipsStyle(QsciScintilla.CallTipsNoContext)
        self.setCallTipsVisible(0)
        self.setCallTipsPosition(QsciScintilla.CallTipsAboveText)
        if self.file_type == FileType.Python:
            self.pylexer = PyCustomLexer(self)
            self.file_open = True
            self.pylexer.setDefaultFont(self.font)
            self.is_auto_file = True
            # Api AUTOCOMPLETION
            # API
            self.__api = QsciAPIs(self.pylexer)
            #autocompletion_image = QPixmap(os.path.join(sys.path[0], "UI/icons/close_icon.png"))
            #self.registerImage(1, autocompletion_image)
            self.auto_completer = PyAutoCompleter(self.full_path,self.__api)
            self.auto_completer.finished.connect(self.loaded_autocomp)
            self.setLexer(self.pylexer)
        elif self.file_type == FileType.Cpp:
            self.cpplexer = CppCustomLexer(self)
            self.file_open = True
            self.cpplexer.setDefaultFont(self.font)
            self.is_auto_file = True
            # Api AUTOCOMPLETION
            # API
            self.__api = QsciAPIs(self.cpplexer)
            #autocompletion_image = QPixmap(os.path.join(sys.path[0], "UI/icons/close_icon.png"))
            #self.registerImage(1, autocompletion_image)
            self.auto_completer = AutoCompleter(self.full_path, self.__api)
            self.auto_completer.finished.connect(self.loaded_autocomp)
            self.setLexer(self.cpplexer)
        elif self.file_type == FileType.C:
            self.clexer = CCustomLexer(self)
            self.file_open = True
            self.clexer.setDefaultFont(self.font)
            self.is_auto_file = True
            # Api AUTOCOMPLETION
            # API
            self.__api = QsciAPIs(self.clexer)
            #autocompletion_image = QPixmap(os.path.join(sys.path[0], "UI/icons/close_icon.png"))
            #self.registerImage(1, autocompletion_image)
            self.auto_completer = AutoCompleter(self.full_path, self.__api)
            self.auto_completer.finished.connect(self.loaded_autocomp)
            self.setLexer(self.clexer)
        elif self.file_type == FileType.Json:
            self.jsonlexer = JsonLexer(self)
            self.jsonlexer.setDefaultFont(self.font)
            self.setLexer(self.jsonlexer)
            self.file_open = True
            self.is_auto_file = False
        else:
            self.file_open = True
            # self.lexer = QsciLexer()
            self.setPaper(QColor("#282c34"))
            self.setColor(QColor("#abb2bf"))
            # self.lexer.setDefaultColor("#abb2bf")
            # self.lexer.setDefaultFont(QFont("Consolas", 14))
            # self.setLexer(self.lexer)
        # style
        load_theme(self,current_theme[2])
        #Marker - Margin
        self.breakpoint_margin = 0
        self.setMarginType(self.breakpoint_margin, QsciScintilla.SymbolMargin)
        self.setMarginWidth(self.breakpoint_margin, 16)
        self.setMarginSensitivity(self.breakpoint_margin, True)
        self.setMarginWidth(self.breakpoint_margin, 16)
        self.setMarginSensitivity(self.breakpoint_margin, True)
        self.markerDefine(QsciScintilla.Circle, 0)
        self.setMarkerBackgroundColor(QColor("#FF0000"), 0)
        self.setMarkerForegroundColor(QColor("#FFFFFF"), 0)
        self.marginClicked.connect(self.on_margin_clicked)
        self.setMarginType(1, QsciScintilla.NumberMargin)
        self.setMarginWidth(1, "0000")
        self.setMarginsFont(self.font)
        self.setMarginSensitivity(1, True)
    def on_margin_clicked(self, margin, line, state):
        if margin == self.breakpoint_margin:  # Left-side margin for breakpoints
            # Check for existing markers
            if self.markersAtLine(line) != 0:
                self.markerDelete(line, self.breakpoint_margin)
            else:
                self.markerAdd(line, self.breakpoint_margin)
    def return_lang_name(self):
        return self.lang_name
    @property
    def current_file_changed(self):
        if self.logsys_on:
            print(self.file_type,self.lang_name, self.main_window.current_file)
            return self._current_file_changed
        else:
              return self._current_file_changed
    @current_file_changed.setter
    def current_file_changed(self, value: bool):
        curr_indx = self.main_window.tab_view.currentIndex()
        if value:
            self.main_window.tab_view.setTabText(curr_indx, "*" + self.path.name)
            self.main_window.setWindowTitle(f"*{self.path.name} - {self.main_window.app_name}")
        else:
            if self.main_window.tab_view.tabText(curr_indx).startswith("*"):
                self.main_window.tab_view.setTabText(
                    curr_indx, 
                    self.main_window.tab_view.tabText(curr_indx)[1:]
                )
                self.main_window.setWindowTitle(self.main_window.windowTitle()[1:])
        self._current_file_changed = value
    @property 
    def autocomplete(self):
        return self.complete_flag
    @autocomplete.setter
    def set_autocomplete(self, value):
        self.complete_flag = value
    def toggle_comment(self, text: str) -> str:
        lines = text.split('\n')
        toggled_lines = []
        for line in lines:
            if line.startswith('#'):
                toggled_lines.append(line[1:].lstrip())
            else:
                toggled_lines.append('# ' + line)
        return '\n'.join(toggled_lines)
    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Space:
            if self.is_python_file:
                pos = self.getCursorPosition()
                self.auto_completer.get_completion(pos[0]+1, pos[1], self.text())
                self.autoCompleteFromAPIs()
                return       
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_X:
            if not self.hasSelectedText():
                line, index = self.getCursorPosition()
                self.setSelection(line, 0, line, self.lineLength(line))
                self.cut()
                return 
        if e.modifiers() == Qt.ControlModifier and e.text() == "/": 
            if self.hasSelectedText():
                start, startl, end, endl = self.getSelection()
                self.setSelection(start, 0, end, self.lineLength(end)-1)
                self.replaceSelectedText(self.toggle_comment(self.selectedText()))
                self.setSelection(start, startl, end, endl)
            else:
                line, idx = self.getCursorPosition()
                self.setSelection(line, 0, line, self.lineLength(line)-1)
                self.replaceSelectedText(self.toggle_comment(self.selectedText()))
                self.setSelection(-1, -1, -1, -1)  
            return 
        return super().keyPressEvent(e)
    def cursorPositionChangedCustom(self, line: int, index: int) -> None:
        if self.is_auto_file:
            self.auto_completer.get_completion(line+1, index, self.text())
    def loaded_autocomp(self):
        pass
    def textChangedCustom(self) -> None:
        if not self.current_file_changed and not self.first_launch:
            self.current_file_changed = True
        if self.first_launch:
            self.first_launch = False