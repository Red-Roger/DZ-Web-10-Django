import psycopg2
import json
import os

from quoteapp.models import Authors, Quotes


path_a = os.getcwd() + '\\quoteapp\\authors.json'
path_q = os.getcwd() + '\\quoteapp\\quotes.json'

path_db = 'dbname=postgres user=postgres password=root'

conn = psycopg2.connect(path_db)


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



conn.commit()
conn.close()


