from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class ThemeTableWidget(QWidget):
    def __init__(self, themes, parent=None):
        super(ThemeTableWidget, self).__init__(parent)
        self.themes = themes
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create QTableWidget
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(len(self.themes))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Theme Name", "Theme Path", "Theme Filename", "Editor Theme Filename"])

        # Populate the table with data
        for row, theme in enumerate(self.themes):
            self.table_widget.setItem(row, 0, QTableWidgetItem(theme['theme_name']))
            self.table_widget.setItem(row, 1, QTableWidgetItem(theme['theme_path']))
            self.table_widget.setItem(row, 2, QTableWidgetItem(theme['theme_filename']))
            self.table_widget.setItem(row, 3, QTableWidgetItem(theme['editor_theme_filename']))

        layout.addWidget(self.table_widget)
        self.setLayout(layout)