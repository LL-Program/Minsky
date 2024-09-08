import os
import json
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QColor
from Settings.datapaths import STYLES_PATH, DATA_PATH
from UI.defaultassets import THEMES

def find_minskytheme_files(defaultfilter : bool):
    themes = []
    search_directory = None
    if defaultfilter:
        search_directory = STYLES_PATH + 'default/themes/'
    else:
        search_directory = STYLES_PATH + 'themes/'
    for root, dirs, files in os.walk(search_directory):
        if "MINSKYTHEME" in files:
            minskytheme_path = os.path.join(root, "MINSKYTHEME")
            with open(minskytheme_path, 'r') as file:
                try:
                    data = json.load(file)
                    theme_name = data.get('theme_name')
                    theme_filename = data.get('theme_filename')
                    editor_theme_filename = data.get('editor_theme_filename')
                    author_theme = data.get('author')
                    version_theme = data.get('version')
                    if theme_name and theme_filename and editor_theme_filename:
                        themes.append({
                            "theme_name": theme_name,
                            "theme_path": root,
                            "theme_filename": theme_filename,
                            "editor_theme_filename": editor_theme_filename,
                            "author" : author_theme,
                            "version" : version_theme
                        })
                    else:
                        return

                except json.JSONDecodeError as e:
                    print(f"Error reading JSON from {minskytheme_path}: {e}")

    return themes
def load_theme(Editor, jsons):
        theme = json.loads(jsons)
        theme = theme["editor-theme"]

        background_color = QColor(theme["paper_color"])

        # Set background color for the entire editor
        Editor.setPaper(background_color)

        # Set default style background
        Editor.SendScintilla(Editor.SCI_STYLESETBACK, Editor.STYLE_DEFAULT, background_color)

        # Apply background color to all relevant styles
        for style in range(128):  # 128 covers a wide range of standard styles
            Editor.SendScintilla(Editor.SCI_STYLESETBACK, style, background_color)

        # Apply other settings
        Editor.setIndentationGuidesBackgroundColor(QColor(theme["indentation_guides_background"]))
        Editor.setIndentationGuidesForegroundColor(QColor(theme["indentation_guides_foreground"]))
        Editor.setEdgeColor(QColor(theme["edge_color"]))
        Editor.setEdgeMode(QsciScintilla.EdgeLine)
        Editor.setWhitespaceBackgroundColor(QColor(theme["whitespace_background"]))
        Editor.setWhitespaceForegroundColor(QColor(theme["whitespace_foreground"]))
        Editor.setSelectionBackgroundColor(QColor(theme["selection_background"]))

        # Call tip colors
        Editor.setCallTipsBackgroundColor(QColor(theme["call_tips_background"]))
        Editor.setCallTipsForegroundColor(QColor(theme["call_tips_foreground"]))
        Editor.setCallTipsHighlightColor(QColor(theme["call_tips_highlight"]))

        # Caret settings
        Editor.setCaretForegroundColor(QColor(theme["caret_foreground"]))
        Editor.setCaretLineVisible(theme["caret_line_visible"])
        Editor.setCaretWidth(theme["caret_width"])
        Editor.setCaretLineBackgroundColor(QColor(theme["caret_line_background"]))

        # Brace matching
        Editor.setMatchedBraceBackgroundColor(QColor(theme["matched_brace_background"]))
        Editor.setMatchedBraceForegroundColor(QColor(theme["matched_brace_foreground"]))

        # Margins and fold margin colors
        Editor.setMarginsForegroundColor(QColor(theme["margins_foreground_color"]))
        Editor.setMarginsBackgroundColor(QColor(theme["margins_background_color"]))
        Editor.setFoldMarginColors(QColor(theme["fold_margin_foreground_color"]), QColor(theme["fold_margin_background_color"]))

        # Line number margin
        Editor.setMarginType(0, QsciScintilla.NumberMargin)
        Editor.setMarginWidth(0, "00000")  # Adjust width as needed
        Editor.setMarginsBackgroundColor(QColor(theme["line_number_background"]))
        Editor.setMarginsForegroundColor(QColor(theme["line_number_foreground"]))

        # Fold margin indicators
        Editor.setFoldMarginColors(QColor(theme["fold_indicator_background"]), QColor(theme["fold_indicator_foreground"]))

        # Set EOL mode
        eol_mode = theme.get("eol_mode", "EolWindows")
        if eol_mode == "EolWindows":
            Editor.setEolMode(QsciScintilla.EolWindows)
        elif eol_mode == "EolUnix":
            Editor.setEolMode(QsciScintilla.EolUnix)
        elif eol_mode == "EolMac":
            Editor.setEolMode(QsciScintilla.EolMac)

        Editor.setEolVisibility(theme["eol_visibility"])
def readStylesJson(Branche):
     styles = DATA_PATH + 'styles.json'
     with open(styles, "r") as f: theme_json = json.load(f)
     return theme_json.get(Branche)
def get_Style():
    styles = DATA_PATH + 'styles.json'
    with open(styles, "r") as f: theme_json = json.load(f)
    name = theme_json["theme"]
    defaulttheme = theme_json["default-theme"]
    if defaulttheme:
        for theme in THEMES:
            if name == theme[0]:
                return theme
#Variables
current_theme = get_Style()

def applyEditortheme(tab_widget,jsons):
    for i in range(tab_widget.count()):
            editor = tab_widget.widget(i)
            load_theme(editor, jsons)
def loadLexers():
    # Define the path to the lexers directory
    lexers_path = os.path.join(STYLES_PATH, 'lexers')
    
    # Initialize an empty list to store lexer dictionaries
    lexer_list = []

    # Check if the directory exists
    if not os.path.exists(lexers_path):
        print(f"Directory {lexers_path} does not exist.")
        return lexer_list

    # Iterate over all files in the lexers directory
    for filename in os.listdir(lexers_path):
        if filename.endswith('.json'):
            # Construct the full file path
            file_path = os.path.join(lexers_path, filename)

            # Open and read the JSON file
            with open(file_path, 'r') as file:
                try:
                    # Load the JSON data into a Python dictionary
                    data = json.load(file)

                    # Add the entire theme content to the lexer_list
                    lexer_dict = {
                        'name': data.get('theme', {}).get('name', 'Unknown'),
                        'version': data.get('theme', {}).get('version', 'Unknown'),
                        'theme_content': data  # Store the entire JSON content
                    }

                    # Append the dictionary to the lexer_list
                    lexer_list.append(lexer_dict)

                except json.JSONDecodeError as e:
                    print(f"Failed to decode JSON from {filename}: {e}")

    # Return the list of lexer dictionaries
    return lexer_list
def applyCurrentLexer(Lexer):
    lexer_name = readStylesJson("lexer")
    lexers = loadLexers()
    for item in lexers:
        if item["name"] == lexer_name:
            return item["theme_content"]  # Returning theme content as dict
    return None  # Return None if no lexer is found
