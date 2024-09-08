#TOMMOROW NIGHT BLUE
TOMMOROW_NIGHT_BLUE_UI = """
QMainWindow {
    background-color: #002451;
    color: #ffffff;
    border-radius: 0px;
    border: none;
}

Heading {
    background-color: #002451;
}

QStatusBar {
    background-color: #002451;
    height: 200ex;
}

QTabWidget {
    background-color: #002451;
    color: #ffffff;
}

QTabBar::tab {
    background-color: #00346e;
    color: #a0a0a0;
    border: none;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
    padding: 2px;
    min-width: 50ex;
    min-height: 10ex;
    font-size: 12px;
}

QTabBar::tab:selected {
    background-color: #00579a;
    color: #ffffff;
    font-weight: bold;
}

QTabBar::tab:!selected {
    margin-top: 2px; /* Make non-selected tabs a bit higher */
}

QTabBar::close-button {
    image: url(F:/Projects/Minsky/src/UI/icons/close-icon.svg);
}

QSplitter {
    background-color: #002451;
}

QSplitter::handle {
    background-color: #00346e;
}

QScrollBar:vertical {
    border: none;
    width: 14px;
    margin: 15px 0 15px 0;
    background-color: #00346e;
    border-radius: 0px;
}

QScrollBar::handle:vertical {
    background-color: #4f9fcf;
}

QScrollBar::handle:vertical:hover {
    background-color: #007acc;
}

QScrollBar::handle:vertical:pressed {
    background-color: #007acc;
}

QScrollBar::sub-line:vertical {
    border: none;
    background: none;
    height: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical {
    border: none;
    background: none;
    height: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:horizontal {
    border: none;
    height: 14px;
    margin: 0px 0 0 0;
    background-color: #00346e;
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #4f9fcf;
}

QScrollBar::handle:horizontal:hover {
    background-color: #007acc;
}

QScrollBar::handle:horizontal:pressed {
    background-color: #007acc;
}

QScrollBar::sub-line:horizontal {
    border: none;
    background: none;
    width: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal {
    border: none;
    background: none;
    width: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QsciScintilla#Editor {
    border: none;
    background-color: #002451;
    color: #ffffff;
}

QMessageBox {
    color: #ffffff;
    border-radius: 30px;
}

QLineEdit {
    background-color: #001f33;
    border-radius: 4px;
    border: 1px solid #004080;
    padding: 3px;
    color: #ffffff;
    min-height: 6ex;
}

QLineEdit::hover {
    color: #ffffff;
}

QListView, QTreeView {
    background-color: #002451;
    border-radius: 5px;
    border: 1px solid #004080;
    padding: 5px;
    color: #ffffff;
}

QListView::item:hover, QTreeView::item:hover {
    background-color: #00346e;
    border: 1px solid #004080;
    border-radius: 3px;
    color: #ffffff;
}

QListView::item:selected, QTreeView::item:selected {
    background-color: #004080;
    border-style: none;
    color: #ffffff;
}

QTreeView::item {
    border: 1px solid transparent;
}

QMenuBar {
    color: #ffffff;
    font-size: 16px;
    border: none;
    outline: none;
}

QMenuBar::item:selected {
    background-color: rgba(255, 255, 255, 0.1);
}

QMenuBar::item {
    margin-top: 0;
    padding: 2px 6px;
    border-radius: 5px;
}

QMenu {
    background-color: #002451;
    padding: 5px;
    color: #ffffff;
    font-size: 15px;
    border: none;
    outline: none;
}

QMenu::item {
    background-color: #002451;
    padding: 3px;
    color: #ffffff;
    font-size: 14px;
    border-radius: 20px;
}

QMenu::item:selected {
    background-color: #00346e;
}

QPushButton#wlcmbutton1 {
    color: #8246fa;
    background-color: transparent;
    height: 20px;
    font-size: 15px;
    font-family: 'Consolas';
}

QPushButton#wlcmbutton1:hover {
    font-size: 17px;
}

QPushButton#wlcmbutton1:pressed {
    border: 4px solid #006bb3;
}

QStatusBar::item {
    border: none;
}

QStatusBar#MinskyStatusBar {
    color: #ffffff;
    height: 22px;
}

QStatusBar#MinskyStatusBarbutton {
    background: transparent;
    border: none;
}

QFrame#MinskyLanguageFrame {
    background-color: #001f33;
    border: none;
    color: #ffffff;
}

QFrame#MinskyLanguageFrame::hover {
    color: #ffffff;
}

QFrame#MinskyCentralWidget {
    background: #002451;
    border-radius: 0px;
}

QToolTip {
    background-color: #00346e;
    border: none;
    color: #ffffff;
}

QTextEdit#MinskyLogSystem {
    background: #002451;
    border-radius: 0px;
}

QTextEdit#CodeTerminal {
    background-color: #002451;
    color: #ffffff;
    font-family: Consolas;
    font-size: 12pt;
}
QLabel#CurrentDir{
    font-size: 14px;
    background-color: #002451;
    font-weight: bold;
    color: #ffffff;
    text-align:center;
}
QFrame#TerminalHeading{
    background-color: #002451;  # Dark blue background color
    border: none;
    border-radius: 5px;  # Rounded corners
}

"""
TOMMOROW_NIGHT_BLUE_EDITOR = """
{
    "editor-theme": {
        "paper_color": "#002451",
        "indentation_guides_background": "#002451",
        "indentation_guides_foreground": "#666666",
        "style_default_background": "#002451",
        "edge_color": "#003f8e",
        "whitespace_background": "#003f8e",
        "whitespace_foreground": "#4f5b66",
        "selection_background": "#003f8e",
        "call_tips_background": "#002451",
        "call_tips_foreground": "#c0c5ce",
        "call_tips_highlight": "#bf616a",
        "caret_foreground": "#c0c5ce",
        "caret_line_background": "#003f8e",
        "matched_brace_background": "#a3be8c",
        "matched_brace_foreground": "#f99157",
        "caret_width": 2,
        "caret_line_visible": true,
        "eol_mode": "EolWindows",
        "eol_visibility": false,
        "margins_foreground_color": "#ff888888",
        "margins_background_color": "#282c34",
        "fold_margin_background_color": "#2c313c",
        "fold_margin_foreground_color": "#2c313c",
        "line_number_foreground": "#4f5b66",
        "line_number_background": "#002451",
        "fold_indicator_foreground": "#4f5b66",
        "fold_indicator_background": "#002451"
    }
}
"""
TOMMOROW_NIGHT_BLUE = ["Tommorow Night Blue",TOMMOROW_NIGHT_BLUE_UI,TOMMOROW_NIGHT_BLUE_EDITOR]
#DESERTDAY
DESERT_DAY_UI = """
    QMainWindow {
    background-color: #e0c097;  /* Sandy beige */
    color: #5a3e2b;  /* Desert brown */
    border-radius: 0px;
    border: none;
}

Heading {
    background-color: #e0c097;  /* Sandy beige */
}

QStatusBar {
    background-color: #e0c097;  /* Sandy beige */
    height: 200ex;
}

QTabWidget {
    background-color: #e0c097;  /* Sandy beige */
    color: #5a3e2b;  /* Desert brown */
}

QTabBar::tab {
    background-color: #d8a85f;  /* Sandy orange */
    color: #5a3e2b;  /* Desert brown */
    border: none;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
    padding: 2px;
    min-width: 50ex;
    min-height: 10ex;
    font-size: 12px;
}

QTabBar::tab:selected {
    background-color: #c87f3a;  /* Warm brown */
    color: #ffffff;  /* White for selected tab text */
    font-weight: bold;
}

QTabBar::tab:!selected {
    margin-top: 2px; /* Make non-selected tabs a bit higher */
}

QTabBar::close-button {
    image: url(F:/Projects/Minsky/src/UI/icons/close-icon.svg);
}

QSplitter {
    background-color: #e0c097;  /* Sandy beige */
}

QSplitter::handle {
    background-color: #d8a85f;  /* Sandy orange */
}

QScrollBar:vertical {
    border: none;
    width: 14px;
    margin: 15px 0 15px 0;
    background-color: #d8a85f;  /* Sandy orange */
    border-radius: 0px;
}

QScrollBar::handle:vertical {
    background-color: #b27835;  /* Earthy brown */
}

QScrollBar::handle:vertical:hover {
    background-color: #c87f3a;  /* Warm brown */
}

QScrollBar::handle:vertical:pressed {
    background-color: #c87f3a;  /* Warm brown */
}

QScrollBar::sub-line:vertical {
    border: none;
    background: none;
    height: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical {
    border: none;
    background: none;
    height: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:horizontal {
    border: none;
    height: 14px;
    margin: 0px 0 0 0;
    background-color: #d8a85f;  /* Sandy orange */
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #b27835;  /* Earthy brown */
}

QScrollBar::handle:horizontal:hover {
    background-color: #c87f3a;  /* Warm brown */
}

QScrollBar::handle:horizontal:pressed {
    background-color: #c87f3a;  /* Warm brown */
}

QScrollBar::sub-line:horizontal {
    border: none;
    background: none;
    width: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal {
    border: none;
    background: none;
    width: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QsciScintilla#Editor {
    border: none;
    background-color: #e0c097;  /* Sandy beige */
    color: #5a3e2b;  /* Desert brown */
}

QMessageBox {
    color: #5a3e2b;  /* Desert brown */
    border-radius: 30px;
}

QLineEdit {
    background-color: #d4ab76;  /* Light desert brown */
    border-radius: 4px;
    border: 1px solid #a3752e;  /* Deep desert brown */
    padding: 3px;
    color: #5a3e2b;  /* Desert brown */
    min-height: 6ex;
}

QLineEdit::hover {
    color: #5a3e2b;  /* Desert brown */
}

QListView, QTreeView {
    background-color: #e0c097;  /* Sandy beige */
    border-radius: 5px;
    border: 1px solid #a3752e;  /* Deep desert brown */
    padding: 5px;
    color: #5a3e2b;  /* Desert brown */
}

QListView::item:hover, QTreeView::item:hover {
    background-color: #d8a85f;  /* Sandy orange */
    border: 1px solid #a3752e;  /* Deep desert brown */
    border-radius: 3px;
    color: #5a3e2b;  /* Desert brown */
}

QListView::item:selected, QTreeView::item:selected {
    background-color: #a3752e;  /* Deep desert brown */
    border-style: none;
    color: #ffffff;  /* White text on selection */
}

QTreeView::item {
    border: 1px solid transparent;
}

QMenuBar {
    color: #5a3e2b;  /* Desert brown */
    font-size: 16px;
    border: none;
    outline: none;
}

QMenuBar::item:selected {
    background-color: rgba(255, 255, 255, 0.1);
}

QMenuBar::item {
    margin-top: 0;
    padding: 2px 6px;
    border-radius: 5px;
}

QMenu {
    background-color: #e0c097;  /* Sandy beige */
    padding: 5px;
    color: #5a3e2b;  /* Desert brown */
    font-size: 15px;
    border: none;
    outline: none;
}

QMenu::item {
    background-color: #e0c097;  /* Sandy beige */
    padding: 3px;
    color: #5a3e2b;  /* Desert brown */
    font-size: 14px;
    border-radius: 20px;
}

QMenu::item:selected {
    background-color: #d8a85f;  /* Sandy orange */
}

QPushButton#wlcmbutton1 {
    color: #8b5e34;  /* Warm brown */
    background-color: transparent;
    height: 20px;
    font-size: 15px;
    font-family: 'Consolas';
}

QPushButton#wlcmbutton1:hover {
    font-size: 17px;
}

QPushButton#wlcmbutton1:pressed {
    border: 4px solid #a3752e;  /* Deep desert brown */
}

QStatusBar::item {
    border: none;
}

QStatusBar#MinskyStatusBar {
    color: #5a3e2b;  /* Desert brown */
    height: 22px;
}

QStatusBar#MinskyStatusBarbutton {
    background: transparent;
    border: none;
}

QFrame#MinskyLanguageFrame {
    background-color: #d4ab76;  /* Light desert brown */
    border: none;
    color: #5a3e2b;  /* Desert brown */
}

QFrame#MinskyLanguageFrame::hover {
    color: #5a3e2b;  /* Desert brown */
}

QFrame#MinskyCentralWidget {
    background: #e0c097;  /* Sandy beige */
    border-radius: 0px;
}

QToolTip {
    background-color: #d8a85f;  /* Sandy orange */
    border: none;
    color: #ffffff;  /* White text */
}

QTextEdit#MinskyLogSystem {
    background: #e0c097;  /* Sandy beige */
    border-radius: 0px;
}

QTextEdit#CodeTerminal {
    background-color: #e0c097;  /* Sandy beige */
    color: #5a3e2b;  /* Desert brown */
    font-family: Consolas;
    font-size: 12pt;
}

QLabel#CurrentDir {
    font-size: 14px;
    background-color: #e0c097;  /* Sandy beige */
    font-weight: bold;
    color: #5a3e2b;  /* Desert brown */
    text-align: center;
}

QFrame#TerminalHeading {
    background-color: #e0c097;  /* Sandy beige */
    border: none;
    border-radius: 5px;  /* Rounded corners */
}
"""
DESERT_DAY_EDITOR = """
    {
    "editor-theme": {
        "paper_color": "#e0c097",  /* Sandy beige */
        "indentation_guides_background": "#e0c097",  /* Sandy beige */
        "indentation_guides_foreground": "#a3752e",  /* Deep desert brown */
        "style_default_background": "#e0c097",  /* Sandy beige */
        "edge_color": "#d8a85f",  /* Sandy orange */
        "whitespace_background": "#d8a85f",  /* Sandy orange */
        "whitespace_foreground": "#b27835",  /* Earthy brown */
        "selection_background": "#d8a85f",  /* Sandy orange */
        "call_tips_background": "#e0c097",  /* Sandy beige */
        "call_tips_foreground": "#5a3e2b",  /* Desert brown */
        "call_tips_highlight": "#c87f3a",  /* Warm brown */
        "caret_foreground": "#5a3e2b",  /* Desert brown */
        "caret_line_background": "#d8a85f",  /* Sandy orange */
        "matched_brace_background": "#a3752e",  /* Deep desert brown */
        "matched_brace_foreground": "#c87f3a",  /* Warm brown */
        "caret_width": 2,
        "caret_line_visible": true,
        "eol_mode": "EolWindows",
        "eol_visibility": false,
        "margins_foreground_color": "#ffb27835",  /* Earthy brown with transparency */
        "margins_background_color": "#e0c097",  /* Sandy beige */
        "fold_margin_background_color": "#d4ab76",  /* Light desert brown */
        "fold_margin_foreground_color": "#d4ab76",  /* Light desert brown */
        "line_number_foreground": "#a3752e",  /* Deep desert brown */
        "line_number_background": "#e0c097",  /* Sandy beige */
        "fold_indicator_foreground": "#a3752e",  /* Deep desert brown */
        "fold_indicator_background": "#e0c097"  /* Sandy beige */
    }
}
"""
DESERT_DAY = ["Desert Day",DESERT_DAY_UI, DESERT_DAY_EDITOR]
#Coding Night
CODING_NIGHT_UI = """
QMainWindow {
    background-color: #1e1e1e;
    color: #ffffff;
    border-radius: 0px;
    border: none;
}

Heading {
    background-color: #1e1e1e;
}

QStatusBar {
    background-color: #1e1e1e;
    height: 200ex;
}
QStatusBar::item {
    border: none;
}
QTabWidget {
    background-color: #1e1e1e;
    color: #ffffff;
}

QTabBar::tab {
    background-color: #2a2a2a;
    color: #c0c0c0;
    border: none;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
    padding: 2px;
    min-width: 50ex;
    min-height: 10ex;
    font-size: 12px;
}

QTabBar::tab:selected {
    background-color: #3a3a3a;
    color: #ffffff;
    font-weight: bold;
}

QTabBar::tab:!selected {
    margin-top: 2px;
}

QTabBar::close-button {
    image: url(F:/Projects/Minsky/src/UI/icons/close-icon.svg);
}

QSplitter {
    background-color: #1e1e1e;
}

QSplitter::handle {
    background-color: #2a2a2a;
}

QScrollBar:vertical {
    border: none;
    width: 14px;
    margin: 15px 0 15px 0;
    background-color: #2a2a2a;
    border-radius: 0px;
}

QScrollBar::handle:vertical {
    background-color: #3e3e3e;
}

QScrollBar::handle:vertical:hover {
    background-color: #4f4f4f;
}

QScrollBar::handle:vertical:pressed {
    background-color: #4f4f4f;
}

QScrollBar::sub-line:vertical {
    border: none;
    background: none;
    height: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical {
    border: none;
    background: none;
    height: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:horizontal {
    border: none;
    height: 14px;
    margin: 0px 0 0 0;
    background-color: #2a2a2a;
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #3e3e3e;
}

QScrollBar::handle:horizontal:hover {
    background-color: #4f4f4f;
}

QScrollBar::handle:horizontal:pressed {
    background-color: #4f4f4f;
}

QScrollBar::sub-line:horizontal {
    border: none;
    background: none;
    width: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal {
    border: none;
    background: none;
    width: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QsciScintilla#Editor {
    border: none;
    background-color: #1e1e1e;
    color: #ffffff;
}

QMessageBox {
    color: #ffffff;
    border-radius: 30px;
}

QLineEdit {
    background-color: #2a2a2a;
    border-radius: 4px;
    border: 1px solid #3e3e3e;
    padding: 3px;
    color: #ffffff;
    min-height: 6ex;
}

QLineEdit::hover {
    color: #ffffff;
}

QListView, QTreeView {
    background-color: #1e1e1e;
    border-radius: 5px;
    border: 1px solid #3e3e3e;
    padding: 5px;
    color: #ffffff;
}

QListView::item:hover, QTreeView::item:hover {
    background-color: #2a2a2a;
    border: 1px solid #3e3e3e;
    border-radius: 3px;
    color: #ffffff;
}

QListView::item:selected, QTreeView::item:selected {
    background-color: #3e3e3e;
    border-style: none;
    color: #ffffff;
}

QTreeView::item {
    border: 1px solid transparent;
}

QMenuBar {
    color: #ffffff;
    font-size: 16px;
    border: none;
    outline: none;
}

QMenuBar::item:selected {
    background-color: rgba(255, 255, 255, 0.1);
}

QMenuBar::item {
    margin-top: 0;
    padding: 2px 6px;
    border-radius: 5px;
}

QMenu {
    background-color: #1e1e1e;
    padding: 5px;
    color: #ffffff;
    font-size: 15px;
    border: none;
    outline: none;
}

QMenu::item {
    background-color: #1e1e1e;
    padding: 3px;
    color: #ffffff;
    font-size: 14px;
    border-radius: 20px;
}

QMenu::item:selected {
    background-color: #2a2a2a;
}

QPushButton#wlcmbutton1 {
    color: #8246fa;
    background-color: transparent;
    height: 20px;
    font-size: 15px;
    font-family: 'Consolas';
}

QPushButton#wlcmbutton1:hover {
    font-size: 17px;
}

QPushButton#wlcmbutton1:pressed {
    border: 4px solid #4f4f4f;
}

QStatusBar::item {
    border: none;
}

QStatusBar#MinskyStatusBar {
    color: #ffffff;
    height: 22px;
}

QStatusBar#MinskyStatusBarbutton {
    background: transparent;
    border: none;
}

QFrame#MinskyLanguageFrame {
    background-color: #2a2a2a;
    border: none;
    color: #ffffff;
}

QFrame#MinskyLanguageFrame::hover {
    color: #ffffff;
}

QFrame#MinskyCentralWidget {
    background: #1e1e1e;
    border-radius: 0px;
}

QToolTip {
    background-color: #2a2a2a;
    border: none;
    color: #ffffff;
}

QTextEdit#MinskyLogSystem {
    background: #1e1e1e;
    border-radius: 0px;
}

QTextEdit#CodeTerminal {
    background-color: #1e1e1e;
    color: #ffffff;
    font-family: Consolas;
    font-size: 12pt;
}

QLabel#CurrentDir {
    font-size: 14px;
    background-color: #1e1e1e;
    font-weight: bold;
    color: #ffffff;
    text-align: center;
}

QFrame#TerminalHeading {
    background-color: #1e1e1e;
    border: none;
    border-radius: 5px;
}
QLabel#AlertWidget {
    background-color: rgba(0, 0, 0, 0.8); 
    color: white; padding: 10px; 
    border-radius: 5px;
}
"""
CODING_NIGHT_EDITOR = """
{
    "editor-theme": {
        "paper_color": "#1e1e1e",
        "indentation_guides_background": "#1e1e1e",
        "indentation_guides_foreground": "#3e3e3e",
        "style_default_background": "#1e1e1e",
        "edge_color": "#3a3a3a",
        "whitespace_background": "#3a3a3a",
        "whitespace_foreground": "#555555",
        "selection_background": "#264f78",
        "call_tips_background": "#2d2d2d",
        "call_tips_foreground": "#c0c0c0",
        "call_tips_highlight": "#ff6a6a",
        "caret_foreground": "#c0c0c0",
        "caret_line_background": "#2d2d2d",
        "matched_brace_background": "#444444",
        "matched_brace_foreground": "#ffcc66",
        "caret_width": 2,
        "caret_line_visible": true,
        "eol_mode": "EolWindows",
        "eol_visibility": false,
        "margins_foreground_color": "#888888",
        "margins_background_color": "#2a2a2a",
        "fold_margin_background_color": "#2a2a2a",
        "fold_margin_foreground_color": "#888888",
        "line_number_foreground": "#555555",
        "line_number_background": "#1e1e1e",
        "fold_indicator_foreground": "#555555",
        "fold_indicator_background": "#1e1e1e"
    }
}

"""
CODING_NIGHT = ["Coding Night", CODING_NIGHT_UI, CODING_NIGHT_EDITOR]

OCEAN_BREEZE_UI = """
QMainWindow {
    background-color: #102027;
    color: #e0f7fa;
    border-radius: 0px;
    border: none;
}

Heading {
    background-color: #102027;
}

QStatusBar {
    background-color: #102027;
    height: 200ex;
}
QStatusBar::item {
    border: none;
}
QTabWidget {
    background-color: #102027;
    color: #e0f7fa;
}

QTabBar::tab {
    background-color: #37474f;
    color: #b2ebf2;
    border: none;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
    padding: 2px;
    min-width: 50ex;
    min-height: 10ex;
    font-size: 12px;
}

QTabBar::tab:selected {
    background-color: #455a64;
    color: #ffffff;
    font-weight: bold;
}

QTabBar::tab:!selected {
    margin-top: 2px;
}

QTabBar::close-button {
    image: url(F:/Projects/Minsky/src/UI/icons/close-icon.svg);
}

QSplitter {
    background-color: #102027;
}

QSplitter::handle {
    background-color: #37474f;
}

QScrollBar:vertical {
    border: none;
    width: 14px;
    margin: 15px 0 15px 0;
    background-color: #37474f;
    border-radius: 0px;
}

QScrollBar::handle:vertical {
    background-color: #546e7a;
}

QScrollBar::handle:vertical:hover {
    background-color: #607d8b;
}

QScrollBar::handle:vertical:pressed {
    background-color: #607d8b;
}

QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
    background: none;
    border: none;
    height: 15px;
}

QScrollBar:horizontal {
    border: none;
    height: 14px;
    background-color: #37474f;
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #546e7a;
}

QScrollBar::handle:horizontal:hover {
    background-color: #607d8b;
}

QScrollBar::handle:horizontal:pressed {
    background-color: #607d8b;
}

QsciScintilla#Editor {
    border: none;
    background-color: #102027;
    color: #e0f7fa;
}

QMessageBox, QMenu, QToolTip {
    color: #e0f7fa;
    background-color: #102027;
    border: none;
}

QLineEdit {
    background-color: #37474f;
    border-radius: 4px;
    border: 1px solid #546e7a;
    padding: 3px;
    color: #e0f7fa;
    min-height: 6ex;
}

QListView, QTreeView {
    background-color: #102027;
    border-radius: 5px;
    border: 1px solid #546e7a;
    padding: 5px;
    color: #e0f7fa;
}

QMenuBar {
    color: #e0f7fa;
    font-size: 16px;
    border: none;
    outline: none;
}

QMenuBar::item:selected {
    background-color: rgba(224, 247, 250, 0.1);
}

QPushButton#wlcmbutton1 {
    color: #00acc1;
    background-color: transparent;
    height: 20px;
    font-size: 15px;
    font-family: 'Consolas';
}

QPushButton#wlcmbutton1:hover {
    font-size: 17px;
}

QPushButton#wlcmbutton1:pressed {
    border: 4px solid #546e7a;
}

QTextEdit#MinskyLogSystem, QTextEdit#CodeTerminal {
    background: #102027;
    color: #e0f7fa;
    font-family: Consolas;
    font-size: 12pt;
}

QLabel#CurrentDir {
    font-size: 14px;
    background-color: #102027;
    font-weight: bold;
    color: #e0f7fa;
    text-align: center;
}

QFrame#TerminalHeading {
    background-color: #102027;
    border: none;
    border-radius: 5px;
}
"""
OCEAN_BREEZE_EDITOR = """
{
    "editor-theme": {
        "paper_color": "#102027",
        "indentation_guides_background": "#102027",
        "indentation_guides_foreground": "#37474f",
        "style_default_background": "#102027",
        "edge_color": "#455a64",
        "whitespace_background": "#37474f",
        "whitespace_foreground": "#607d8b",
        "selection_background": "#455a64",
        "call_tips_background": "#102027",
        "call_tips_foreground": "#e0f7fa",
        "call_tips_highlight": "#00acc1",
        "caret_foreground": "#e0f7fa",
        "caret_line_background": "#455a64",
        "matched_brace_background": "#80deea",
        "matched_brace_foreground": "#ff7043",
        "caret_width": 2,
        "caret_line_visible": true,
        "eol_mode": "EolWindows",
        "eol_visibility": false,
        "margins_foreground_color": "#ff888888",
        "margins_background_color": "#37474f",
        "fold_margin_background_color": "#37474f",
        "fold_margin_foreground_color": "#37474f",
        "line_number_foreground": "#607d8b",
        "line_number_background": "#102027",
        "fold_indicator_foreground": "#607d8b",
        "fold_indicator_background": "#102027"
    }
}
"""
SUNSET_GLOW_UI = """
QMainWindow {
    background-color: #2c1e1e;
    color: #ffcc80;
    border-radius: 0px;
    border: none;
}

Heading {
    background-color: #2c1e1e;
}
QStatusBar::item {
    border: none;
}
QStatusBar {
    background-color: #2c1e1e;
    height: 200ex;
}

QTabWidget {
    background-color: #2c1e1e;
    color: #ffcc80;
}

QTabBar::tab {
    background-color: #4e342e;
    color: #ffab91;
    border: none;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
    padding: 2px;
    min-width: 50ex;
    min-height: 10ex;
    font-size: 12px;
}

QTabBar::tab:selected {
    background-color: #6d4c41;
    color: #ffffff;
    font-weight: bold;
}

QTabBar::tab:!selected {
    margin-top: 2px;
}

QTabBar::close-button {
    image: url(F:/Projects/Minsky/src/UI/icons/close-icon.svg);
}

QSplitter {
    background-color: #2c1e1e;
}

QSplitter::handle {
    background-color: #4e342e;
}

QScrollBar:vertical {
    border: none;
    width: 14px;
    margin: 15px 0 15px 0;
    background-color: #4e342e;
    border-radius: 0px;
}

QScrollBar::handle:vertical {
    background-color: #795548;
}

QScrollBar::handle:vertical:hover {
    background-color: #8d6e63;
}

QScrollBar::handle:vertical:pressed {
    background-color: #8d6e63;
}

QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
    background: none;
    border: none;
    height: 15px;
}

QScrollBar:horizontal {
    border: none;
    height: 14px;
    background-color: #4e342e;
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #795548;
}

QScrollBar::handle:horizontal:hover {
    background-color: #8d6e63;
}

QsciScintilla#Editor {
    border: none;
    background-color: #2c1e1e;
    color: #ffcc80;
}

QMessageBox, QMenu, QToolTip {
    color: #ffcc80;
    background-color: #2c1e1e;
    border: none;
}

QLineEdit {
    background-color: #4e342e;
    border-radius: 4px;
    border: 1px solid #6d4c41;
    padding: 3px;
    color: #ffcc80;
    min-height: 6ex;
}

QListView, QTreeView {
    background-color: #2c1e1e;
    border-radius: 5px;
    border: 1px solid #6d4c41;
    padding: 5px;
    color: #ffcc80;
}

QMenuBar {
    color: #ffcc80;
    font-size: 16px;
    border: none;
    outline: none;
}

QMenuBar::item:selected {
    background-color: rgba(255, 204, 128, 0.1);
}

QPushButton#wlcmbutton1 {
    color: #ff5722;
    background-color: transparent;
    height: 20px;
    font-size: 15px;
    font-family: 'Consolas';
}

QPushButton#wlcmbutton1:hover {
    font-size: 17px;
}

QPushButton#wlcmbutton1:pressed {
    border: 4px solid #6d4c41;
}

QTextEdit#MinskyLogSystem, QTextEdit#CodeTerminal {
    background: #2c1e1e;
    color: #ffcc80;
    font-family: Consolas;
    font-size: 12pt;
}

QLabel#CurrentDir {
    font-size: 14px;
    background-color: #2c1e1e;
    font-weight: bold;
    color: #ffcc80;
    text-align: center;
}

QFrame#TerminalHeading {
    background-color: #2c1e1e;
    border: none;
    border-radius: 5px;
}
"""
SUNSET_GLOW_EDITOR = """
{
    "editor-theme": {
        "paper_color": "#2c1e1e",
        "indentation_guides_background": "#2c1e1e",
        "indentation_guides_foreground": "#4e342e",
        "style_default_background": "#2c1e1e",
        "edge_color": "#6d4c41",
        "whitespace_background": "#4e342e",
        "whitespace_foreground": "#8d6e63",
        "selection_background": "#6d4c41",
        "call_tips_background": "#2c1e1e",
        "call_tips_foreground": "#ffcc80",
        "call_tips_highlight": "#ff5722",
        "caret_foreground": "#ffcc80",
        "caret_line_background": "#6d4c41",
        "matched_brace_background": "#ffab91",
        "matched_brace_foreground": "#ff7043",
        "caret_width": 2,
        "caret_line_visible": true,
        "eol_mode": "EolWindows",
        "eol_visibility": false,
        "margins_foreground_color": "#ff888888",
        "margins_background_color": "#4e342e",
        "fold_margin_background_color": "#4e342e",
        "fold_margin_foreground_color": "#4e342e",
        "line_number_foreground": "#8d6e63",
        "line_number_background": "#2c1e1e",
        "fold_indicator_foreground": "#8d6e63",
        "fold_indicator_background": "#2c1e1e"
    }
}
"""

FOREST_GREEN_UI = """
QMainWindow {
    background-color: #1b2b1d;
    color: #c5e1a5;
    border-radius: 0px;
    border: none;
}

Heading {
    background-color: #1b2b1d;
}

QStatusBar {
    background-color: #1b2b1d;
    height: 200ex;
}
QStatusBar::item {
    border: none;
}
QTabWidget {
    background-color: #1b2b1d;
    color: #c5e1a5;
}

QTabBar::tab {
    background-color: #33691e;
    color: #aed581;
    border: none;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
    padding: 2px;
    min-width: 50ex;
    min-height: 10ex;
    font-size: 12px;
}

QTabBar::tab:selected {
    background-color: #558b2f;
    color: #ffffff;
    font-weight: bold;
}

QTabBar::tab:!selected {
    margin-top: 2px;
}

QTabBar::close-button {
    image: url(F:/Projects/Minsky/src/UI/icons/close-icon.svg);
}

QSplitter {
    background-color: #1b2b1d;
}

QSplitter::handle {
    background-color: #33691e;
}

QScrollBar:vertical {
    border: none;
    width: 14px;
    margin: 15px 0 15px 0;
    background-color: #33691e;
    border-radius: 0px;
}

QScrollBar::handle:vertical {
    background-color: #558b2f;
}

QScrollBar::handle:vertical:hover {
    background-color: #689f38;
}

QScrollBar::handle:vertical:pressed {
    background-color: #689f38;
}

QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
    background: none;
    border: none;
    height: 15px;
}

QScrollBar:horizontal {
    border: none;
    height: 14px;
    background-color: #33691e;
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #558b2f;
}

QScrollBar::handle:horizontal:hover {
    background-color: #689f38;
}

QsciScintilla#Editor {
    border: none;
    background-color: #1b2b1d;
    color: #c5e1a5;
}

QMessageBox, QMenu, QToolTip {
    color: #c5e1a5;
    background-color: #1b2b1d;
    border: none;
}

QLineEdit {
    background-color: #33691e;
    border-radius: 4px;
    border: 1px solid #558b2f;
    padding: 3px;
    color: #c5e1a5;
    min-height: 6ex;
}

QListView, QTreeView {
    background-color: #1b2b1d;
    border-radius: 5px;
    border: 1px solid #558b2f;
    padding: 5px;
    color: #c5e1a5;
}

QMenuBar {
    color: #c5e1a5;
    font-size: 16px;
    border: none;
    outline: none;
}

QMenuBar::item:selected {
    background-color: rgba(197, 225, 165, 0.1);
}

QPushButton#wlcmbutton1 {
    color: #7cb342;
    background-color: transparent;
    height: 20px;
    font-size: 15px;
    font-family: 'Consolas';
}

QPushButton#wlcmbutton1:hover {
    font-size: 17px;
}

QPushButton#wlcmbutton1:pressed {
    border: 4px solid #558b2f;
}

QTextEdit#MinskyLogSystem, QTextEdit#CodeTerminal {
    background: #1b2b1d;
    color: #c5e1a5;
    font-family: Consolas;
    font-size: 12pt;
}

QLabel#CurrentDir {
    font-size: 14px;
    background-color: #1b2b1d;
    font-weight: bold;
    color: #c5e1a5;
    text-align: center;
}

QFrame#TerminalHeading {
    background-color: #1b2b1d;
    border: none;
    border-radius: 5px;
}
"""
FOREST_GREEN_EDITOR = """
{
    "editor-theme": {
        "paper_color": "#1b2b1d",
        "indentation_guides_background": "#1b2b1d",
        "indentation_guides_foreground": "#33691e",
        "style_default_background": "#1b2b1d",
        "edge_color": "#558b2f",
        "whitespace_background": "#33691e",
        "whitespace_foreground": "#689f38",
        "selection_background": "#558b2f",
        "call_tips_background": "#1b2b1d",
        "call_tips_foreground": "#c5e1a5",
        "call_tips_highlight": "#7cb342",
        "caret_foreground": "#c5e1a5",
        "caret_line_background": "#558b2f",
        "matched_brace_background": "#aed581",
        "matched_brace_foreground": "#ffcc80",
        "caret_width": 2,
        "caret_line_visible": true,
        "eol_mode": "EolWindows",
        "eol_visibility": false,
        "margins_foreground_color": "#ff888888",
        "margins_background_color": "#33691e",
        "fold_margin_background_color": "#33691e",
        "fold_margin_foreground_color": "#33691e",
        "line_number_foreground": "#689f38",
        "line_number_background": "#1b2b1d",
        "fold_indicator_foreground": "#689f38",
        "fold_indicator_background": "#1b2b1d"
    }
}
"""

CYBERPUNK_NEON_UI = """
QMainWindow {
    background-color: #000000;
    color: #00ff99;
    border-radius: 0px;
    border: none;
}

Heading {
    background-color: #000000;
}

QStatusBar {
    background-color: #000000;
    height: 200ex;
}
QStatusBar::item {
    border: none;
}
QTabWidget {
    background-color: #000000;
    color: #00ff99;
}

QTabBar::tab {
    background-color: #1a1a1a;
    color: #00ff99;
    border: none;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
    padding: 2px;
    min-width: 50ex;
    min-height: 10ex;
    font-size: 12px;
}

QTabBar::tab:selected {
    background-color: #333333;
    color: #00ffcc;
    font-weight: bold;
}

QTabBar::tab:!selected {
    margin-top: 2px;
}

QTabBar::close-button {
    image: url(F:/Projects/Minsky/src/UI/icons/close-icon.svg);
}

QSplitter {
    background-color: #000000;
}

QSplitter::handle {
    background-color: #1a1a1a;
}

QScrollBar:vertical {
    border: none;
    width: 14px;
    margin: 15px 0 15px 0;
    background-color: #1a1a1a;
    border-radius: 0px;
}

QScrollBar::handle:vertical {
    background-color: #333333;
}

QScrollBar::handle:vertical:hover {
    background-color: #4d4d4d;
}

QScrollBar::handle:vertical:pressed {
    background-color: #4d4d4d;
}

QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
    background: none;
    border: none;
    height: 15px;
}

QScrollBar:horizontal {
    border: none;
    height: 14px;
    background-color: #1a1a1a;
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #333333;
}

QScrollBar::handle:horizontal:hover {
    background-color: #4d4d4d;
}

QsciScintilla#Editor {
    border: none;
    background-color: #000000;
    color: #00ff99;
}

QMessageBox, QMenu, QToolTip {
    color: #00ff99;
    background-color: #000000;
    border: none;
}

QLineEdit {
    background-color: #1a1a1a;
    border-radius: 4px;
    border: 1px solid #333333;
    padding: 3px;
    color: #00ff99;
    min-height: 6ex;
}

QListView, QTreeView {
    background-color: #000000;
    border-radius: 5px;
    border: 1px solid #333333;
    padding: 5px;
    color: #00ff99;
}

QMenuBar {
    color: #00ff99;
    font-size: 16px;
    border: none;
    outline: none;
}

QMenuBar::item:selected {
    background-color: rgba(0, 255, 153, 0.1);
}

QPushButton#wlcmbutton1 {
    color: #ff00ff;
    background-color: transparent;
    height: 20px;
    font-size: 15px;
    font-family: 'Consolas';
}

QPushButton#wlcmbutton1:hover {
    font-size: 17px;
}

QPushButton#wlcmbutton1:pressed {
    border: 4px solid #333333;
}

QTextEdit#MinskyLogSystem, QTextEdit#CodeTerminal {
    background: #000000;
    color: #00ff99;
    font-family: Consolas;
    font-size: 12pt;
}

QLabel#CurrentDir {
    font-size: 14px;
    background-color: #000000;
    font-weight: bold;
    color: #00ff99;
    text-align: center;
}

QFrame#TerminalHeading {
    background-color: #000000;
    border: none;
    border-radius: 5px;
}
"""
CYBERPUNK_NEON_EDITOR = """
{
    "editor-theme": {
        "paper_color": "#000000",
        "indentation_guides_background": "#000000",
        "indentation_guides_foreground": "#1a1a1a",
        "style_default_background": "#000000",
        "edge_color": "#333333",
        "whitespace_background": "#1a1a1a",
        "whitespace_foreground": "#4d4d4d",
        "selection_background": "#333333",
        "call_tips_background": "#000000",
        "call_tips_foreground": "#00ff99",
        "call_tips_highlight": "#ff00ff",
        "caret_foreground": "#00ff99",
        "caret_line_background": "#333333",
        "matched_brace_background": "#ff00ff",
        "matched_brace_foreground": "#00ffcc",
        "caret_width": 2,
        "caret_line_visible": true,
        "eol_mode": "EolWindows",
        "eol_visibility": false,
        "margins_foreground_color": "#ff888888",
        "margins_background_color": "#1a1a1a",
        "fold_margin_background_color": "#1a1a1a",
        "fold_margin_foreground_color": "#1a1a1a",
        "line_number_foreground": "#4d4d4d",
        "line_number_background": "#000000",
        "fold_indicator_foreground": "#4d4d4d",
        "fold_indicator_background": "#000000"
    }
}
"""

OZEAN_BREEZE = ["Ozean Breeze", OCEAN_BREEZE_UI, OCEAN_BREEZE_EDITOR]
SUNSET_GLOW = ["Sunset Glow", SUNSET_GLOW_UI, SUNSET_GLOW_EDITOR]
FOREST_GREEN = ["Forest Green", FOREST_GREEN_UI, FOREST_GREEN_EDITOR]
CYBERPUNK_NEON = ["Cyberpunk Neon", CYBERPUNK_NEON_UI, CYBERPUNK_NEON_EDITOR]
#-----------------Themes-------------
THEMES = [CODING_NIGHT,TOMMOROW_NIGHT_BLUE,OZEAN_BREEZE,SUNSET_GLOW,FOREST_GREEN,CYBERPUNK_NEON]
