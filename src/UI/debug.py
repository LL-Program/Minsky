import os
from Filesystem.file_types import FileType
import webbrowser
#For Alpha Tests...
def runwoutd(file, type):
    if file == None:
       return
    if type == FileType.Python:
        os.system(f"python {file}")
    if type == FileType.Html:
       webbrowser.open(file) 