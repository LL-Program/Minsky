from Lexer.lexer import MinskyLexer
import builtins
import types

class CppCustomLexer(MinskyLexer):
    """Custom lexer for C++"""
    def __init__(self, editor):
        super(CppCustomLexer, self).__init__("C++", editor)
        self.Author = "Lukas Rennhofer"
        self.setKeywords([
            "alignas", "alignof", "and", "and_eq", "asm", "auto", "bitand", "bitor", "bool",
            "break", "case", "catch", "char", "char16_t", "char32_t", "class", "compl", "const",
            "constexpr", "const_cast", "continue", "decltype", "default", "delete", "do", "double",
            "dynamic_cast", "else", "enum", "explicit", "export", "extern", "false", "float", "for",
            "friend", "goto", "if", "inline", "int", "long", "mutable", "namespace", "new", "noexcept",
            "nullptr", "operator", "private", "protected", "public", "register", "reinterpret_cast",
            "return", "short", "signed", "sizeof", "static", "static_assert", "static_cast", "struct",
            "switch", "template", "this", "thread_local", "throw", "true", "try", "typedef", "typeid",
            "typename", "union", "unsigned", "using", "virtual", "void", "volatile", "wchar_t",
            "while"
        ])
        self.setBuiltinNames([
            name
            for name, obj in vars(builtins).items()
            if isinstance(obj, types.BuiltinFunctionType)
        ])

    def styleText(self, start, end):
        """Apply syntax highlighting to the text between start and end positions."""
        self.startStyling(start)

        text = self.editor.text()[start:end]
        self.generate_tokens(text)

        # Flags for handling multi-line strings and comments
        string_flag = False
        comment_flag = False

        while True:
            curr_token = self.next_tok()
            if curr_token is None:
                break

            tok: str = curr_token[0]
            tok_len: int = curr_token[1]

            # Handle single-line comments
            if tok.startswith("//"):
                self.setStyling(tok_len, self.COMMENTS)
                comment_flag = True
                continue

            # Handle multi-line comments
            if tok.startswith("/*"):
                self.setStyling(tok_len, self.COMMENTS)
                comment_flag = True
                # Process the rest of the comment block
                while True:
                    curr_token = self.next_tok()
                    if curr_token is None:
                        break
                    tok = curr_token[0]
                    tok_len = curr_token[1]
                    self.setStyling(tok_len, self.COMMENTS)
                    if tok.endswith("*/"):
                        comment_flag = False
                        break
                continue

            # Handle strings
            if tok == '"' or tok == "'":
                self.setStyling(tok_len, self.STRING)
                string_flag = True
                # Process the rest of the string
                while True:
                    curr_token = self.next_tok()
                    if curr_token is None:
                        break
                    tok = curr_token[0]
                    tok_len = curr_token[1]
                    self.setStyling(tok_len, self.STRING)
                    if tok.endswith('"') or tok.endswith("'"):
                        string_flag = False
                        break
                continue

            if comment_flag:
                self.setStyling(tok_len, self.COMMENTS)
                continue

            if string_flag:
                self.setStyling(tok_len, self.STRING)
                continue

            if tok in self.keywords_list:
                self.setStyling(tok_len, self.KEYWORD)
                continue

            if tok.isidentifier():
                self.setStyling(tok_len, self.DEFAULT)
                continue

            if tok.isnumeric():
                self.setStyling(tok_len, self.CONSTANTS)
                continue

            if tok in ["(", ")", "{", "}", "[", "]"]:
                self.setStyling(tok_len, self.BRACKETS)
                continue

            if tok in ["+", "-", "*", "/", "%", "=", "<", ">", "==", "!=", "<=", ">=", "&&", "||", "++", "--"]:
                self.setStyling(tok_len, self.TYPES)
                continue

            # Default handling for all other cases
            self.setStyling(tok_len, self.DEFAULT)
