# Filesystem/__init__.py

# Import the main components of the filesystem package
from .file_types import FileType

# Define what should be accessible when using `from Filesystem import *`
__all__ = ['FileType']
