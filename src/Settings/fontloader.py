from PyQt5.QtGui import QFontDatabase
import json
from Settings.datapaths import DATA_PATH,STYLES_PATH

def load_fonts():
    styles = DATA_PATH + "styles.json"
    with open(styles, "r") as f: theme_json = json.load(f)
    fonts = theme_json["fonts"]
    for font in fonts:
        QFontDatabase.addApplicationFont(STYLES_PATH + str(font.values()))
