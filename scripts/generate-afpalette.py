import os
import json
import zipfile
import xml.etree.ElementTree as ET

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    lv = len(hex)
    return tuple(int(hex[i:i + lv // 3], 16) / 255.0 for i in range(0, lv, lv // 3))

def create_afpalette(colors, output_path):
    palette = ET.Element("palette")
    palette.set("type", "document")
    for color in colors:
        swatch = ET.SubElement(palette, "swatch")
        swatch.set("name", color["name"])
        swatch.set("type", "fill")
        swatch.set("space", "rgb")
        r, g, b = hex_to_rgb(color["hex"])
        swatch.set("r", str(r))
        swatch.set("g", str(g))
        swatch.set("b", str(b))

    tree = ET.ElementTree(palette)
    temp_dir = "temp_afpalette"
    os.makedirs(temp_dir, exist_ok=True)
    xml_path = os.path.join(temp_dir, "data.xml")
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(xml_path, arcname="data.xml")

    os.remove(xml_path)
    os.rmdir(temp_dir)

with open("palettes/brand-palette.json") as f:
    colors = json.load(f)

create_afpalette(colors, "palettes/brand-palette.afpalette")
