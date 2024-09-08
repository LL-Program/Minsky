# Lexer/__init__.py

# Import the main components of the lexer system
from .lexer import MinskyLexer
from .LexerManager import LexerManager, register_lexer

# Optionally, you can also import specific lexers if you want them accessible at the package level
# This is useful if you want users to be able to do something like: `from Lexer import PyCustomLexer`
# But this is typically not needed if lexers are dynamically loaded via `LexerManager`
# from .py_custom_lexer import PyCustomLexer

# Define what should be accessible when using `from Lexer import *`
__all__ = ['MinskyLexer', 'LexerManager', 'register_lexer']
