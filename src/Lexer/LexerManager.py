import os
import importlib.util
from PyQt5.Qsci import QsciAPIs
from Filesystem.file_types import FileType
from PyQt5.QtGui import QColor
from Editor.autocompleter import AutoCompleter
# This will serve as a registry for lexers
LEXER_REGISTRY = {}

def register_lexer(file_type):
    """Decorator to register a lexer class for a given file type."""
    def decorator(cls):
        LEXER_REGISTRY[file_type] = cls
        print(f"Registered lexer for {file_type}: {cls}")
        return cls
    return decorator


class LexerManager:
    def __init__(self, editor, file_type, font, full_path):
        self.editor = editor
        self.file_type = file_type
        self.font = font
        self.full_path = full_path
        self.lexer = None
        self.__api = None

    def load_lexer(self):
        lexer_class = LEXER_REGISTRY.get(self.file_type)
        if lexer_class:
            print(f"Loading lexer: {lexer_class}")
            self.lexer = lexer_class(self.editor)
            self.lexer.setDefaultFont(self.font)
            self.editor.setLexer(self.lexer)
        else:
            print(f"No lexer found for file type: {self.file_type}")

    def setup_autocompletion(self):
        if self.file_type in [FileType.Python, FileType.Cpp, FileType.C]:
            self.__api = QsciAPIs(self.lexer)
            self.auto_completer = AutoCompleter(self.full_path, self.__api)
            self.auto_completer.finished.connect(self.editor.loaded_autocomp)

