from WebAPI.version_h import *

#get new version infos

class VersionSettings:
    VERSION = get_versionapi('version')
    TESTPHASE = get_versionapi('testphase')
    CONTRIBUTERS = get_versionapi('Contributers')
    UI_TITLE = get_versionapi('title')
    UI_BODY = get_versionapi('body')
    CHANGELOGS_LINK = get_versionapi('Changelogs')


