import psycopg2
import json
import os
from operator import itemgetter

from quoteapp.models import Authors, Quotes


path_a = os.getcwd() + '\\quoteapp\\authors.json'
path_q = os.getcwd() + '\\quoteapp\\quotes.json'
path_html = os.getcwd() + '\\quoteapp\\templates\\quoteapp\\index.html'
path_start = os.getcwd() + '\\quoteapp\\start_page'
path_end = os.getcwd() + '\\quoteapp\\end_page'
path_middle = os.getcwd() + '\\quoteapp\\middle_page'
path_db = 'dbname=postgres user=postgres password=root'
path_views = os.getcwd() + '\\quoteapp\\views.py'
path_urls = os.getcwd() + '\\quoteapp\\urls.py'

conn = psycopg2.connect(path_db)
div_text = ''
count_tegs = {}

with open(path_a, 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        if not Authors.objects.filter(fullname = item["fullname"]):
            Authors.objects.create (fullname = item["fullname"], born_date = item["born_date"], born_location = item["born_location"], description = item["description"])
            with open(path_views, 'a', encoding="utf-8") as file1:
                file1.write(f"\rdef {item["fullname"].replace(" ","").replace(".","")}(request):\r    return render(request, 'quoteapp/author/{item["fullname"]}.html')\r\r")    
        
        path_about = os.getcwd() + f'\\quoteapp\\templates\\quoteapp\\author\\{item["fullname"]}.html'
        about_text = f"<div class=\"author-details\">\r    <h3 class=\"author-title\">{item["fullname"]}</h3>\r"
        about_text += f"    <p><strong>Born:</strong> <span class=\"author-born-date\">{item["born_date"]}</span> <span class=\"author-born-location\">{item["born_location"]}</span></p>\r"
        about_text += f"    <p><strong>Description:</strong></p>\r    <div class=\"author-description\">\r    "
        about_text += f"{item["description"]}\r    </div>\r</div>\r\r    </div>\r\r</body>\r</html>"
        
        with open(path_start, 'r') as file1:
            data1 = file1.read()    
        data1 += about_text 
          
        with open(path_about, 'w',encoding="utf-8") as file1:
            file1.write(data1)

with open(path_q, 'r') as json_file:
    data = json.load(json_file)
    div_text += "<div class=\"row\">\r    <div class=\"col-md-8\">\r"
    for item in data:
        if not Quotes.objects.filter(quote = item["quote"]):
            inst = Authors.objects.get(fullname = item["author"])
            Quotes.objects.create (tags = item["tags"], author = inst, quote = item["quote"])
        
        div_text += "\r    <div class=\"quote\" itemscope itemtype=\"http://schema.org/CreativeWork\">\r        <span class=\"text\" itemprop=\"text\">"
        div_text += f"{item["quote"]}</span>"
        div_text += f"\r        <span>by <small class=\"author\" itemprop=\"author\">{item["author"]}</small>"
        div_text += f"\r        <a href=\"./author/{item["author"]}.html\">(about)</a>\r        </span>\r"
        div_text += "        <div class=\"tags\">\r            Tags:"
        temp = ""
        for el in item["tags"]:
            temp += el
            temp += ","
            if el in count_tegs:
                count_tegs[el] += 1
            else:
                count_tegs[el] = 1
        temp = temp[:-1]
        div_text += f"<meta class=\"keywords\" itemprop=\"keywords\" content=\"{temp}\" /    >\r\r"
        for el in item["tags"]:
            div_text += f"            <a class=\"tag\" href=\"/tag/change/page/1/\">{el}</a>\r\r"
        div_text +="        </div>\r    </div>\r"

conn.commit()
conn.close()

sorted_tags = dict(sorted(count_tegs.items(), key=itemgetter(1), reverse=True))
new_data = ""
with open(path_end, 'r') as file1:
    data = file1.read()
    new_data = data[:325]
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 28px\" href=\"/tag/{list(sorted_tags)[0]}/\">{list(sorted_tags)[0]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 26px\" href=\"/tag/{list(sorted_tags)[1]}/\">{list(sorted_tags)[1]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 26px\" href=\"/tag/{list(sorted_tags)[2]}/\">{list(sorted_tags)[2]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 24px\" href=\"/tag/{list(sorted_tags)[3]}/\">{list(sorted_tags)[3]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 22px\" href=\"/tag/{list(sorted_tags)[4]}/\">{list(sorted_tags)[4]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 14px\" href=\"/tag/{list(sorted_tags)[5]}/\">{list(sorted_tags)[5]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 10px\" href=\"/tag/{list(sorted_tags)[6]}/\">{list(sorted_tags)[6]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 8px\" href=\"/tag/{list(sorted_tags)[7]}/\">{list(sorted_tags)[7]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 8px\" href=\"/tag/{list(sorted_tags)[8]}/\">{list(sorted_tags)[8]}</a>\r            </span>\r"
    new_data += f"\r            <span class=\"tag-item\">\r            <a class=\"tag\" style=\"font-size: 6px\" href=\"/tag/{list(sorted_tags)[9]}/\">{list(sorted_tags)[9]}</a>\r            </span>\r"
    new_data += "    </div>\r</div>\r\r    </div>\r</body>\r</html>"

with open(path_end, 'w', encoding="utf-8") as file1:
    file1.write(new_data)

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

