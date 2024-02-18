import psycopg2
import json
import os

from quoteapp.models import Authors, Quotes


path_a = os.getcwd() + '\\quoteapp\\authors.json'
path_q = os.getcwd() + '\\quoteapp\\quotes.json'
path_html = os.getcwd() + '\\quoteapp\\templates\\quoteapp\\main.html'
path_start = os.getcwd() + '\\quoteapp\\start_page'
path_end = os.getcwd() + '\\quoteapp\\end_page'
path_middle = os.getcwd() + '\\quoteapp\\middle_page'
path_db = 'dbname=postgres user=postgres password=root'

conn = psycopg2.connect(path_db)
div_text = ''

with open(path_a, 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        if not Authors.objects.filter(fullname = item["fullname"]):
            Authors.objects.create (fullname = item["fullname"], born_date = item["born_date"], born_location = item["born_location"], description = item["description"])

with open(path_q, 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        if not Quotes.objects.filter(quote = item["quote"]):
            inst = Authors.objects.get(fullname = item["author"])
            Quotes.objects.create (tags = item["tags"], author = inst, quote = item["quote"])
        div_text += "\r    <div class=\"quote\" itemscope itemtype=\"http://schema.org/CreativeWork\">\r        <span class=\"text\" itemprop=\"text\">"
        div_text += f"{item["quote"]}</span>"
        div_text += f"\r        <span>by <small class=\"author\" itemprop=\"author\">{item["author"]}</small>"
        div_text += f"\r        <a href=\"/author/{item["author"]}\">(about)</a>\r        </span>\r"
        div_text += "        <div class=\"tags\">\r            Tags:"
        temp = ""
        for el in item["tags"]:
            temp += el
            temp += ","
        temp = temp[:-1]
        div_text += f"<meta class=\"keywords\" itemprop=\"keywords\" content=\"{temp}\" /    >\r\r"
        for el in item["tags"]:
            div_text += f"            <a class=\"tag\" href=\"/tag/change/page/1/\">{el}</a>\r\r"
        div_text +="        </div>\r    </div>\r"

conn.commit()
conn.close()

with open(path_middle, 'w', encoding="utf-8") as file1:
    file1.write(div_text)

with open(path_start, 'r') as file1:
    data = file1.read()

with open(path_middle, 'r') as file1:
    data += file1.read()

with open(path_end, 'r') as file1:
    data += file1.read()

with open(path_html, 'w') as file1:
    file1.write(data)





