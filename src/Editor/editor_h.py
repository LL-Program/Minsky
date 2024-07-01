from typing import TYPE_CHECKING

from pathlib import Path
from PyQt5.Qsci import QsciScintilla, QsciAPIs
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QKeyEvent, QFontDatabase, QImage
from UI.debug import *
from LLS.lexer import PyCustomLexer, JsonLexer
from Filesystem.file_types import get_file_type,searchfiletype, FileType, get_current_lang
from Editor.autocompleter import AutoCompleter
from PyQt5.QtGui import QPixmap
import sys
if TYPE_CHECKING:
    from UI.Mainwindow import MainWindow


class Editor(QsciScintilla):

    def __init__(self, main_window, parent=None, path: Path = None, file_type=".py", env=None):
        super(Editor, self).__init__(parent)
        self.first_launch = True 
        self.main_window: MainWindow = main_window

        self.path = path
        self.file_type: FileType = get_file_type(searchfiletype(self.main_window.current_file))
        self.lang_name =  get_current_lang(self.file_type)
        main_window.file_type = self.file_type
         
        self.full_path = self.path.absolute()
        self.is_python_file = self.file_type == FileType.Python
        self.venv = env
        self._current_file_changed = False        

        self.cursorPositionChanged.connect(self.cursorPositionChangedCustom)
        self.textChanged.connect(self.textChangedCustom)
        QFontDatabase.addApplicationFont(os.path.join(sys.path[0], 'UI/styles/fonts/zed-mono-extended.ttf'))
             
        self.setUtf8(True)
        
        self.font = QFont('Zed Mono Extended', 14)
        self.setFont(self.font)
        #log-sys-----
        self.logsys_on = False
        #for online Server
        self.linesnumber = self.lines()
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        self.setTabWidth(4)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False) 
        self.setAutoIndent(True)
        self.marker_sysmbol1 = QImage(os.path.join(sys.path[0], "UI/icons/folder_icon.svg"))
        self.markerDefine(self.marker_sysmbol1, 0)
       
        self.setAutoCompletionSource(QsciScintilla.AcsAPIs)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)

        self.setCallTipsStyle(QsciScintilla.CallTipsNoContext)
        self.setCallTipsVisible(0)
        self.setCallTipsPosition(QsciScintilla.CallTipsAboveText)
        
        self.setCallTipsBackgroundColor(QColor(0xff, 0xff, 0xff, 0xff))
     
        self.setCallTipsForegroundColor(QColor(0x50, 0x50, 0x50, 0xff))
     
        self.setCallTipsHighlightColor(QColor(0xff, 0x00, 0x00, 0xff))
        self.setCaretForegroundColor(QColor("#dedcdc"))
        self.setCaretLineVisible(True)
        self.setCaretWidth(2)
        self.setCaretLineBackgroundColor(QColor("#2c313c"))
        self.setMatchedBraceBackgroundColor(QColor("#c678dd"))
        self.setMatchedBraceForegroundColor(QColor("#F2E3E3"))

       
        self.setEolMode(QsciScintilla.EolMode.EolWindows)
        self.setEolVisibility(False)

        if self.file_type == FileType.Python:
         
            self.pylexer = PyCustomLexer(self)
         
            self.pylexer.setDefaultFont(self.font)

            # Api AUTOCOMPLETION
            # API
            self.__api = QsciAPIs(self.pylexer)
            autocompletion_image = QPixmap(os.path.join(sys.path[0], "UI/icons/close-icon.svg"))
            self.registerImage(1, autocompletion_image)

            self.auto_completer = AutoCompleter(self.full_path, self.__api)
            self.auto_completer.finished.connect(self.loaded_autocomp)
            self.setLexer(self.pylexer)

        elif self.file_type == FileType.Json:
            self.jsonlexer = JsonLexer(self)
            self.jsonlexer.setDefaultFont(self.font)
            self.setLexer(self.jsonlexer)
        else:
            self.setPaper(QColor("#282c34"))
            self.setColor(QColor("#abb2bf"))
            self.lexer.setDefaultColor("#abb2bf")
            self.lexer.setDefaultFont(QFont("Zed Mono Extended", 14))
            self.setLexer(self.lexer)

        # style
        self.setIndentationGuidesBackgroundColor(QColor("#dedcdc"))
        self.setIndentationGuidesForegroundColor(QColor("#dedcdc"))
        self.SendScintilla(self.SCI_STYLESETBACK, self.STYLE_DEFAULT, QColor("#282c34"))
        self.setEdgeColor(QColor("#2c313c"))
        self.setEdgeMode(QsciScintilla.EdgeLine)
        self.setWhitespaceBackgroundColor(QColor("#2c313c"))
        self.setWhitespaceForegroundColor(QColor("#ffffff"))
        self.setContentsMargins(0, 0, 0, 0)
        self.setSelectionBackgroundColor(QColor("#333a46"))

        
        self.markerDefine(QsciScintilla.Circle, 1)
        self.setMarkerBackgroundColor(QColor("#FF0000"), 1)
        self.setMarkerForegroundColor(QColor("#FFFFFF"), 1)

       
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, "0000")
        self.setMarginsForegroundColor(QColor("#ff888888"))
        self.setMarginsBackgroundColor(QColor("#282c34"))
        self.setMarginsFont(self.font)
        self.setMarginSensitivity(1, True)
        self.marginClicked.connect(self.marginclick)
        self.setFolding(QsciScintilla.BoxedFoldStyle, 1)
        self.setFoldMarginColors(QColor("#2c313c"), QColor("#2c313c"))
    	
        
        
    def marginclick(self, margin_nr, line_nr, state):
        print("clicked")
        self.markerAdd(line_nr, 0)
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
        if self.is_python_file:
            self.auto_completer.get_completion(line+1, index, self.text())

    def loaded_autocomp(self):
        pass

 
    def textChangedCustom(self) -> None:
        if not self.current_file_changed and not self.first_launch:
            self.current_file_changed = True
        if self.first_launch:
            self.first_launch = False
