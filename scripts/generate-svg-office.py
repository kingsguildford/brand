import json
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Load JSON palette
with open("palettes/brand-palette.json") as f:
    colors = json.load(f)

# SVG Swatches
svg = Element('svg', xmlns="http://www.w3.org/2000/svg", width="300", height=str(len(colors)*40))
for i, color in enumerate(colors):
    rect = SubElement(svg, 'rect', x="10", y=str(i*40+10), width="40", height="30", fill=color['hex'])
    text = SubElement(svg, 'text', x="60", y=str(i*40+30), fill="#000")
    text.text = f"{color['name']} ({color['hex']})"

ElementTree(svg).write("palettes/brand-palette.svg", encoding="utf-8", xml_declaration=True)

# Office Theme XML
office_theme = Element("a:themeElements", attrib={"xmlns:a": "http://schemas.openxmlformats.org/drawingml/2006/main"})
clr_scheme = SubElement(office_theme, "a:clrScheme", name="CustomBrandPalette")
for i, color in enumerate(colors[:12]):
    clr = SubElement(clr_scheme, f"a:accent{i+1}")
    srgb = SubElement(clr, "a:srgbClr", val=color['hex'][1:])

ElementTree(office_theme).write("office/brand-theme.xml", encoding="utf-8", xml_declaration=True)
