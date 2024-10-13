<div align='center'>
    <img src='https://github.com/DiegoAndresRa/Logos/blob/main/HTML_to_MD.png' width='170px'>
    <h1>Table Markdown Extractor</h1>
</div>
A Python tool designed to extract tables from any webpage and convert them into Markdown format. 
Easily integrate extracted tables into your Markdown documents for notes, documentation, or other projects.

## Usage
```bash
$ python your_script.py <URL> <table_appearance>
```
***Parameters:***
- URL: The URL of the webpage containing the HTML table.
- table_appearance: The appearance of the table within the HTML. (1,2,3,...)

**Notes:**
If the script cannot perform a cURL action (e.g., due to network issues or invalid URL), it will exit with a status code of 1.

## How to Use
Clone the repository
```bash
$ git clone https://github.com/DiegoAndresRa/Table-Markdown-Extractor
$ cd Table-Markdown-Extractor
```

Install dependencies
```bash
$ pip install -r requirements.txt
```

Execute the program
```bash
$ python your_script.py <URL> <table_appearance>
```
