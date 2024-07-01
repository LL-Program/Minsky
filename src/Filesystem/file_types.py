from enum import Enum, auto
import pathlib
 


class FileType(Enum):
    Python = auto()
    Json = auto()
    Toml = auto()
    Html = auto()
    svg = auto()
    Other = auto()

def generate_file_mapping(file_type_extensions):
    file_mapping = {}
    for file_type, extensions in file_type_extensions.items():
        for extension in extensions:
            file_mapping[extension] = file_type
    return file_mapping

file_type_extensions = {
    FileType.Python: [".py", ".pyw"],
    FileType.Json: [".json", ".ipynb"],
    FileType.Toml: [".toml"],
    FileType.Html: [".html", ".htm", ".htmx"],
    FileType.svg : [".svg"],
    FileType.Other: [".txt"],
}

file_type_names = {
    FileType.Python: "Python",
    FileType.Json: "Json",
    FileType.Toml: "Toml",
    FileType.Html: "Html",
    FileType.svg : "Svg",
    FileType.Other: "Other",
}

FILE_MAPPING = generate_file_mapping(file_type_extensions)

def get_file_type(file_suffix: str):
    return FILE_MAPPING.get(file_suffix, FileType.Other)
def get_current_lang(type):
        return file_type_names[type]
def searchfiletype(file):
    if file == None:
        return '.py'
    return pathlib.Path(file).suffix
    