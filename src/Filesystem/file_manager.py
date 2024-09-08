from typing import TYPE_CHECKING
from PyQt5.QtWidgets import (
    QTreeView,
    QFileSystemModel,
    QAbstractItemView,
    QLineEdit,
    QSizePolicy,
    QMessageBox,
    QMenu,
    QFileIconProvider
)
from PyQt5.QtCore import Qt, QDir, QModelIndex, QPoint, QFileInfo
from PyQt5.QtGui import QFont, QIcon, QDropEvent, QDragEnterEvent
from pathlib import Path
import shutil
import os
import subprocess
import sys
from Editor.editor_h import Editor
from Filesystem.file_types import FileType, get_file_type,get_current_lang
from Settings.datapaths import FILEI_PATH, ICON_PATH
if TYPE_CHECKING:
    from UI.Mainwindow import MainWindow

class FileIconProvider(QFileIconProvider):
    def icon(self, parameter):
        current_dir =os.path.dirname(os.path.realpath(__file__))
        if isinstance(parameter, QFileInfo):
            info = parameter
            file_type: FileType = get_file_type("."+info.suffix())
            #print(info.suffix())
            if info.isDir():
                try:
                    icon = QIcon(ICON_PATH+"folder.svg")
                    icon.addFile(ICON_PATH+"folder_open.svg", state = icon.On)
                    return icon
                except FileNotFoundError:
                    pass
            #What is this?
            if file_type != FileType.Other:
                try:
                    return QIcon(FILEI_PATH +f"{get_current_lang(file_type)}.svg")
                except FileNotFoundError:
                    pass 
            else:
                try:
                    return QIcon(ICON_PATH+"file.svg")
                except FileNotFoundError:
                    pass
        return super(FileIconProvider, self).icon(parameter)
class FileManager(QTreeView):
    def __init__(self, tab_view, set_new_tab=None, main_window=None):
        super(FileManager, self).__init__(None)
        self.set_new_tab = set_new_tab
        self.tab_view = tab_view
        self.main_window: MainWindow = main_window
        self.is_renaming = False
        self.current_edit_index = None
        self.previous_rename_name = None
        self.manager_font = QFont("FiraCode", 13)
        self.model: QFileSystemModel = QFileSystemModel()
        self.model.setRootPath(os.getcwd())
        self.model.setIconProvider(FileIconProvider())
        self.model.setFilter(
            QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files | QDir.Drives
        )
        self.model.setReadOnly(False)
        self.setFocusPolicy(Qt.NoFocus)
        self.setFont(self.manager_font)
        self.setModel(self.model)
        self.setRootIndex(self.model.index(os.getcwd()))
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QTreeView.SelectRows)
        self.setEditTriggers(QTreeView.EditTrigger.NoEditTriggers)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.clicked.connect(self.tree_view_clicked)
        self.setIndentation(10)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setHeaderHidden(True)
        self.setColumnHidden(1, True)
        self.setColumnHidden(2, True)
        self.setColumnHidden(3, True)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.itemDelegate().closeEditor.connect(self._on_closeEditor)

    def _on_closeEditor(self, editor: QLineEdit):
        if self.is_renaming:
            self.is_editing = False
            self.rename_file_with_index()
    def tree_view_clicked(self, index: QModelIndex):
        path = self.model.filePath(index)
        f = Path(path)
        if f.is_file():
            self.set_new_tab(f)
    def show_dialog(self, title, msg) -> int:
        dialog = QMessageBox(self)
        dialog.setFont(self.manager_font)
        dialog.font().setPointSize(14)
        dialog.setWindowTitle(title)
        dialog.setWindowIcon(QIcon(ICON_PATH+"close-icon.svg"))
        dialog.setText(msg)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        dialog.setIcon(QMessageBox.Warning)
        return dialog.exec_()
    def show_context_menu(self, pos: QPoint):
        ix = self.indexAt(pos)
        menu = QMenu()
        menu.addAction("New File")
        menu.addAction("New Folder")
        menu.addAction("Open In File Manager")
        if ix.column() != -1:
            menu.addAction("Rename")
            menu.addAction("Delete")
        action = menu.exec_(self.viewport().mapToGlobal(pos))
        if not action:
            return   
        if action.text() == "Rename":
            self.action_rename(ix)
        elif action.text() == "Delete":
            self.action_delete(ix)
        elif action.text() == "New Folder":
            self.action_new_folder()
        elif action.text() == "New File":
            self.action_new_file(ix)
        elif action.text() == "Open In File Manager":
            self.action_open_in_file_manager(ix)
        else:
            pass 
    def rename_file_with_index(self): 
        new_name = self.model.fileName(self.current_edit_index)
        if self.previous_rename_name == new_name:
            return     
        for editor in self.tab_view.findChildren(Editor):
            if editor.path.name == self.previous_rename_name:
                editor.path = editor.path.parent / new_name
                editor_index = self.tab_view.indexOf(editor)
                prev_tab_name = self.tab_view.tabText(editor_index)
                new_tab_name = "*"+new_name if prev_tab_name.startswith("*") else new_name  
                self.tab_view.setTabText(
                    self.tab_view.indexOf(editor), new_tab_name 
                )
                if self.main_window.tab_view.currentWidget() == editor:
                    self.main_window.setWindowTitle(f"{new_tab_name} - {self.main_window.app_name}")
                self.tab_view.repaint()
                editor.full_path = editor.path.absolute()
                self.main_window.current_file = editor.path
                break
    def action_rename(self, ix: QModelIndex):
        self.edit(ix)
        self.previous_rename_name = self.model.fileName(ix)
        self.is_renaming = True
        self.current_edit_index = ix
    def delete_path(self, path: Path):
        """delete file or folder with path"""
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    def action_delete(self, ix):
        file_name = self.model.fileName(ix)
        dialog = self.show_dialog(
            "Delete", f"Are you sure you want to delete {file_name}?"
        )
        if dialog == QMessageBox.Yes:
            if self.selectionModel().hasSelection():
                for i in self.selectionModel().selectedRows():
                    path = Path(self.model.filePath(i))
                    self.delete_path(path)
                    for editor in self.tab_view.findChildren(Editor):
                        if editor.path.name == path.name:
                            self.tab_view.removeTab(
                                self.tab_view.indexOf(editor)
                            )
    def action_new_file(self, ix: QModelIndex):
        root_path = self.model.rootPath()
        if ix.column() != -1 and self.model.isDir(ix):
            self.expand(ix)
            root_path = self.model.filePath(ix)
        f = Path(root_path) / "file"
        count = 1
        while f.exists():
            f = Path(f.parent / f"file{count}")
            count += 1
        f.touch()
        idx = self.model.index(str(f.absolute()))
        self.edit(idx)
    def action_new_folder(self):
        f = Path(self.model.rootPath()) / "New Folder"
        count = 1
        while f.exists():
            f = Path(f.parent / f"New Folder{count}")
            count += 1
        idx = self.model.mkdir(self.rootIndex(), f.name)
        self.edit(idx)
    def action_open_in_file_manager(self, ix: QModelIndex):
        path = os.path.abspath(self.model.filePath(ix))
        is_dir = self.model.isDir(ix)
        if os.name == 'nt':
             #Windows
            if is_dir:
                subprocess.Popen(f'explorer "{path}"')
            else:
                subprocess.Popen(f'explorer /select,"{path}"')
        elif os.name == 'posix':
             #Linux or MacOS
            if sys.platform == 'darwin':
                 #macOS
                if is_dir:
                    subprocess.Popen(['open', path])
                else:
                    subprocess.Popen(['open', '-R', path])
            else:
                 #Linux
                subprocess.Popen(['xdg-open', os.path.dirname(path)])
        else:
            raise OSError(f'Unsupported OS: {os.name}')
    def dropEvent(self, e: QDropEvent) -> None:
        """Drop event for tree view"""
        root_path = Path(self.model.rootPath())
        if e.mimeData().hasUrls():
            for url in e.mimeData().urls():
                path = Path(url.toLocalFile())
                if path.is_dir():
                    shutil.copytree(path, root_path / path.name)
                else:
                    if root_path.samefile(self.model.rootPath()):
                        idx: QModelIndex = self.indexAt(e.pos())
                        if idx.column() == -1:
                            shutil.move(path, root_path / path.name)
                        else:
                            try:
                                folder_path = Path(self.model.filePath(idx))
                                shutil.move(path, folder_path / path.name)
                            except FileNotFoundError:
                                pass
                    else:
                        shutil.copy(path, root_path / path.name)          
        e.accept()
        return super().dropEvent(e)
    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        """Drag enter event for tree view"""
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()
