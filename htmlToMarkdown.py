from markdownify import markdownify as md
import sys

import html2text

if len(sys.argv) == 1:
    sys.exit(f"Error\nUsage: {sys.argv[0]} file.html")

print("Transforming ...")

with open(sys.argv[1],"r") as file:
    html_code = file.read()

with open("html.md","w") as file:
    file.write(md(html_code))

print("HTML → MD")
