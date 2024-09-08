from Lexer.lexer import MinskyLexer
import keyword
import builtins
import types
from PyQt5.QtCore import QThread
from PyQt5.Qsci import QsciAPIs
from jedi import Script
from jedi.api import Completion

class PyAutoCompleter(QThread):
    def __init__(self, file_path, api):
        super(PyAutoCompleter, self).__init__(None)
        self.file_path = file_path
        self.script: Script = None
        self.api: QsciAPIs = api
        self.completions: list[Completion] = None
        self.line = 0
        self.index = 0
        self.text = ""
    def run(self):
        try:
            self.script: Script =  Script(self.text, path=self.file_path)
            self.completions: list[Completion] = self.script.complete(self.line, self.index)
            self.load_autocomplete(self.completions)
        except Exception as err:
            print("Autocomplete Error:", err)
        self.finished.emit()
    def load_autocomplete(self, completions: list[Completion]):
        self.api.clear()
        [self.api.add(i.name) for i in completions]
        self.api.prepare()
    def get_completion(self, line: int, index: int, text: str):
        self.line = line
        self.index = index
        self.text = text
        self.start()

class PyCustomLexer(MinskyLexer):
    """Custom lexer for python"""
    def __init__(self, editor):
        super(PyCustomLexer, self).__init__("Python", editor)
        self.Author = "Lukas Rennhofer"
        self.setKeywords(keyword.kwlist)
        self.setBuiltinNames([
            name
            for name, obj in vars(builtins).items()
            if isinstance(obj, types.BuiltinFunctionType)
        ])

    def styleText(self, start, end):
      
        self.startStyling(start)

       
        text = self.editor.text()[start:end]
      
        self.generate_tokens(text)

        
        string_flag = False
        comment_flag = False

       
        if start > 0:
            previous_style_nr = self.editor.SendScintilla(self.editor.SCI_GETSTYLEAT, start - 1)
            if previous_style_nr == self.COMMENTS:
                comment_flag = False

        while True:
            curr_token = self.next_tok()
            if curr_token is None:
                break
            
            tok: str = curr_token[0]
            tok_len: int = curr_token[1]

           
            if comment_flag:
                self.setStyling(tok_len, self.COMMENTS)
                if tok.endswith("\n") or tok.startswith('\n'):
                    comment_flag = False
                continue

            if string_flag:
                self.setStyling(curr_token[1], self.STRING)
                if tok == '"' or tok == "'":
                    string_flag = False
                continue

            if tok == "class":
                name, ni = self.skip_spaces_peek()
                brac_or_colon, _ = self.skip_spaces_peek(ni)
                if name[0].isidentifier() and brac_or_colon[0] in (":", "("):
                    self.setStyling(tok_len, self.KEYWORD)
                    _ = self.next_tok(ni)  
                    self.setStyling(name[1] + 1, self.CLASSES)
                    continue
                else:
                    self.setStyling(tok_len, self.KEYWORD)
                    continue
            elif tok == "def":
                name, ni = self.skip_spaces_peek()
                if name[0].isidentifier():
                    self.setStyling(tok_len, self.KEYWORD)
                    _ = self.next_tok(ni)
                    self.setStyling(name[1] + 1, self.FUNCTION_DEF)
                    continue
                else:
                    self.setStyling(tok_len, self.KEYWORD)
                    continue
            elif tok in self.keywords_list:
                self.setStyling(tok_len, self.KEYWORD)
                continue
            elif tok.strip() == "." and self.peek_tok()[0].isidentifier():
                self.setStyling(tok_len, self.DEFAULT)
                curr_token = self.next_tok()
                tok: str = curr_token[0]
                tok_len: int = curr_token[1]
                if self.peek_tok()[0] == "(":
                    self.setStyling(tok_len, self.FUNCTIONS)
                else:
                    self.setStyling(tok_len, self.DEFAULT)
                continue
            elif tok.isnumeric() or tok == "self":
                self.setStyling(tok_len, self.CONSTANTS)
                continue
            elif tok in ["(", ")", "{", "}", "[", "]"]:
                self.setStyling(tok_len, self.BRACKETS)
                continue
            elif tok == '"' or tok == "'":
                self.setStyling(tok_len, self.STRING)
                string_flag = True
                continue
            elif tok == "#":
               
                self.setStyling(tok_len, self.COMMENTS)
                comment_flag = True
            elif tok in self.builtin_names or tok in [
                "+",
                "-",
                "*",
                "/",
                "%",
                "=",
                "<",
                ">",
            ]:
                self.setStyling(tok_len, self.TYPES)
                continue
            else:
                self.setStyling(tok_len, self.DEFAULT)