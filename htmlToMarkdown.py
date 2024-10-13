from markdownify import markdownify as md
from requests import get
import re
import sys


if len(sys.argv) == 1:
    sys.exit(f"Error\nUsage: {sys.argv[0]} file.html num_table")


# Get params
try:
    url = sys.argv[1]
    table = int(sys.argv[2])
except ValueError:
    sys.exit(f"{sys.argv[2]} can't cast to Int")
except IndexError:
    sys.exit(f"Error\nUsage: {sys.argv[0]} file.html num_table")


# Get html
print("Getting html code ...")
try:
    html_response = get(url)
    html = html_response.content.decode("utf-8")
    html = html.splitlines()
except requests.exceptions.MissingSchema as error:
    print(str(error))


# Get table's tags
print("Extracting table's tags index")
bgs = [idx for idx, line in enumerate(html, start=1) 
        if re.search(r"<table[^>]*>", line)]
ends = [idx for idx, line in enumerate(html, start=1) 
        if re.search(r"</table>", line)]


# Get table's code
print(f"Getting table {table}'s code")
try:
    bg = bgs[table - 1]
    end = ends[table - 1]
except IndexError:
    sys.exit("Error: number of table out of bounds")
table_code = [html[line] for line in range(bg, end)]
table_code = " ".join(table_code)


# Transforming
print("HTML -> MD")
with open("table.md", "w") as file:
    file.write(md(table_code))
print("Process finished with exit code 0")
