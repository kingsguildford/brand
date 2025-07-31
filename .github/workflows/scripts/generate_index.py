import os
import urllib.parse

REPO = "kingsguildford/brand"
BRANCH = "main"

def make_link(path):
    encoded = urllib.parse.quote(path)
    return f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{encoded}"

def walk_dir(current_path):
    html = ""
    items = sorted(os.listdir(current_path))
    for item in items:
        if item == ".git" or item.startswith(".") or item == "index.html":
            continue
        full_path = os.path.join(current_path, item)
        rel_path = os.path.relpath(full_path, ".")

        if os.path.isdir(full_path):
            html += f"<li><strong>📁 {item}/</strong><ul>\n"
            html += walk_dir(full_path)
            html += "</ul></li>\n"
        else:
            link = make_link(rel_path)
            html += f'<li>📄 <a href="{link}" download>{item}</a></li>\n'
    return html

# Generate final HTML
print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>KCG Brand Archive</title>
  <style>
    body { font-family: sans-serif; max-width: 800px; margin: 2em auto; }
    ul { list-style-type: none; padding-left: 1em; }
    li { margin: 0.25em 0; }
    a { text-decoration: none; color: #0366d6; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>KCG Brand Archive</h1>
  <p>Click any file below to download it:</p>
  <ul>
""")

print(walk_dir("."))

print("""
  </ul>
</body>
</html>
""")
