import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QMenu, QAction, QSplitter
from PyQt5.QtCore import Qt, QEvent

class CodeTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.tabBar().setMouseTracking(True)
        self.tabBar().installEventFilter(self)
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.RightButton:
            tabIndex = self.tabBar().tabAt(event.pos())
            if tabIndex >= 0:
                self.tabBar().setCurrentIndex(tabIndex)
        return super().eventFilter(obj, event)
    def show_context_menu(self, pos):
        menu = QMenu(self)
        split_action = QAction("Split Tab", self)
        split_action.triggered.connect(self.split_tab)
        menu.addAction(split_action)
        menu.exec_(self.mapToGlobal(pos))
    def split_tab(self):
        current_index = self.currentIndex()
        current_widget = self.widget(current_index)
        new_tab_widget = QTabWidget()
        new_tab_widget.addTab(QWidget(), "New Tab")
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(current_widget)
        splitter.addWidget(new_tab_widget)
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        container = QWidget()
        container.setLayout(layout)
        self.setTabText(current_index, self.tabText(current_index) + " (Split)")
        self.removeTab(current_index)
        self.addTab(container, "Split View")

