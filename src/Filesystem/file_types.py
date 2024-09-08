from enum import Enum, auto
import pathlib

class FileType(Enum):
    Python = auto()
    Json = auto()
    Toml = auto()
    Html = auto()
    Svg = auto()
    Cpp = auto()
    C = auto()
    JavaScript = auto()
    Css = auto()
    Java = auto()
    CSharp = auto()
    Ruby = auto()
    Perl = auto()
    Php = auto()
    Xml = auto()
    Markdown = auto()
    Yaml = auto()
    Sql = auto()
    Shell = auto()
    Exe = auto()
    Other = auto()

file_type_extensions = {
    FileType.Python: [".py", ".pyw"],#
    FileType.Json: [".json", ".ipynb"],#
    FileType.Toml: [".toml"],#
    FileType.Html: [".html", ".htm", ".htmx"],#
    FileType.Svg: [".svg"],#
    FileType.Cpp: [".cpp", ".h", ".hpp", ".cc", ".cxx", ".o"],#
    FileType.C: [".c"],#
    FileType.JavaScript: [".js", ".mjs", ".cjs"],#
    FileType.Css: [".css", ".scss", ".sass", ".less"],#
    FileType.Java: [".java", ".class", ".jar"],#
    FileType.CSharp: [".cs", ".dll"],#
    FileType.Ruby: [".rb", ".erb"],#
    FileType.Perl: [".pl", ".pm"],#
    FileType.Php: [".php", ".phtml"],#
    FileType.Xml: [".xml", ".xsl", ".xsd"],#
    FileType.Markdown: [".md", ".markdown"],#
    FileType.Yaml: [".yaml", ".yml"],#
    FileType.Sql: [".sql"],#
    FileType.Shell: [".sh", ".bash", ".zsh", ".ksh"],#
    FileType.Exe: [".exe"],#
    FileType.Other: [".txt"],#
}

file_type_names = {
    FileType.Python: "Python",
    FileType.Json: "Json",
    FileType.Toml: "Toml",
    FileType.Html: "Html",
    FileType.Svg: "Svg",
    FileType.Cpp: "C++",
    FileType.C: "C",
    FileType.JavaScript: "JavaScript",
    FileType.Css: "CSS",
    FileType.Java: "Java",
    FileType.CSharp: "C#",
    FileType.Ruby: "Ruby",
    FileType.Perl: "Perl",
    FileType.Php: "PHP",
    FileType.Xml: "XML",
    FileType.Markdown: "Markdown",
    FileType.Yaml: "YAML",
    FileType.Sql: "SQL",
    FileType.Shell: "Shell",
    FileType.Exe: "Exe",
    FileType.Other: "Other",
}
#Functions
def generate_file_mapping(file_type_extensions):
    file_mapping = {}
    for file_type, extensions in file_type_extensions.items():
        for extension in extensions:
            file_mapping[extension] = file_type
    return file_mapping
FILE_MAPPING = generate_file_mapping(file_type_extensions)

def get_file_type(file_suffix: str):
    return FILE_MAPPING.get(file_suffix, FileType.Other)
def get_current_lang(type) -> str:
        if type == None:
             return "None"
        return file_type_names[type]
def searchfiletype(file):
    if file == None:
        print("File is None")
        return
    return pathlib.Path(file).suffix
    