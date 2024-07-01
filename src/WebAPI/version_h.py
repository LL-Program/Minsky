import json, urllib.request

def get_versionapi(tile : str) -> str:
    data = urllib.request.urlopen("https://minskydev.netlify.app/version.json").read()
    output = json.loads(data)
    return output[tile]