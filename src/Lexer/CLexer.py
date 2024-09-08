from Lexer.lexer import MinskyLexer

class CCustomLexer(MinskyLexer):
    """Custom lexer for C++"""
    def __init__(self, editor):
        super(CCustomLexer, self).__init__("C", editor)
        self.Author = "Lukas Rennhofer"
        self.c_keywords = [
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'inline',
    'int', 'long', 'register', 'restrict', 'return', 'short', 'signed', 'sizeof',
    'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile',
    'while', '_Alignas', '_Alignof', '_Atomic', '_Bool', '_Complex', '_Generic',
    '_Imaginary', '_Noreturn', '_Static_assert', '_Thread_local'
]       
        self.c_builtin_names = [
    'printf', 'scanf', 'sprintf', 'sscanf', 'fscanf', 'fprintf', 'putchar', 'getchar', 'puts', 'gets',
    'fputs', 'fgets', 'fopen', 'fclose', 'fread', 'fwrite', 'fseek', 'ftell', 'rewind', 'feof', 'ferror',
    'perror', 'malloc', 'calloc', 'realloc', 'free', 'exit', 'atexit', 'system', 'abort', 'abs', 'labs',
    'fabs', 'ceil', 'floor', 'sqrt', 'pow', 'exp', 'log', 'log10', 'sin', 'cos', 'tan', 'asin', 'acos',
    'atan', 'sinh', 'cosh', 'tanh', 'memcpy', 'memmove', 'memcmp', 'memset', 'strcpy', 'strncpy', 'strcat',
    'strncat', 'strcmp', 'strncmp', 'strchr', 'strrchr', 'strstr', 'strlen', 'strtok', 'strdup', 'atoi',
    'atol', 'atof', 'itoa', 'ltoa', 'itoa', 'qsort', 'bsearch', 'time', 'ctime', 'gmtime', 'localtime',
    'strftime', 'asctime', 'difftime', 'mktime', 'rand', 'srand'
]

        self.setKeywords(self.c_keywords)
        self.setBuiltinNames(self.c_builtin_names)

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
