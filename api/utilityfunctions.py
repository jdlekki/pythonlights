import re

def parseAppRoutes(path):
    routes = []
    f = open(path, "r")
    lines = f.readlines()
    for line in lines:
        x = re.finditer("@app\.route\('/([^']*)'",line)
        for match in x:
            routes.append(match.group(1))
    return routes


def hexToRGB(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)
