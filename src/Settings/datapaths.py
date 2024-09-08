import os,sys

BUILD_MODE = False

if BUILD_MODE:
    FILEI_PATH = "_internal/icons/fileicons/"
    ICON_PATH = "_internal/icons/"
    DATA_PATH = "_internal/data/"
    STYLES_PATH = "_internal/styles/"
else:
    FILEI_PATH = os.path.join(sys.path[0], os.path.join(sys.path[0], "UI/icons/fileicons/"))
    ICON_PATH = os.path.join(sys.path[0], os.path.join(sys.path[0], "UI/icons/"))
    DATA_PATH = os.path.join(sys.path[0], os.path.join(sys.path[0], "Settings/data/"))
    STYLES_PATH = os.path.join(sys.path[0], os.path.join(sys.path[0], "UI/styles/"))



