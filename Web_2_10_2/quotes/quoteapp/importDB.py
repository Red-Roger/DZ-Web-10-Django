import psycopg2
import json
import os

from models import Authors


path_a = os.getcwd() + '\\quoteapp\\authors.json'
path_q = os.getcwd() + '\\quoteapp\\quotes.json'

path_db = 'dbname=postgres user=postgres password=root'

conn = psycopg2.connect(path_db)

with open(path_a, 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        Authors.objects.create (fullname = item["fullname"], born_date = item["born_date"], born_location = item["born_location"], description = item["description"])

conn.commit()
conn.close()


