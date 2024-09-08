from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
import json
from Settings.datapaths import DATA_PATH

def getFunction(MainWindow, command):
    functions = {
    "o FileFrame" : MainWindow.save_file,
    "o Terminal" : MainWindow.save_file,
    "s File" : MainWindow.save_file
}
    return functions[command]

def LoadShortcuts(MainWindow):
    shortcutsfile =  DATA_PATH + "shortcuts.json"
    with open(shortcutsfile, "r") as f:
        shortcuts = json.load(f)
    for shortcut in shortcuts["keyShortcuts"]:
        shortcutaction = QShortcut(QKeySequence(shortcut["shortcut"]), MainWindow)
        shortcutaction.activated.connect(getFunction(MainWindow, shortcut["command"]))
def printNames():
    shortcutsfile = DATA_PATH + "shortcuts.json"
    with open(shortcutsfile, "r") as f:
        shortcuts = json.load(f)
    for shortcut in shortcuts["keyShortcuts"]:
        print(shortcut)
