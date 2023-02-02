from csv_json import *
from pymongo import MongoClient

#convertir el csv a json
csvFilePath = r'winemag-data.csv'
jsonFilePath = r'winemag-data.json'
# csv_to_json(csvFilePath, jsonFilePath)


client = MongoClient("mongodb+srv://lab03BD:AleOscarYong01@laboratorio03uvg.7rhri6m.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
db = client.Lab03
winemag = db.winemag

with open(jsonFilePath, 'r') as json_file:
    data = json.load(json_file)
    counter = 0
    for x in data:
        lista = []
        counter = 0
        while counter != 10000:
            counter += 1
            lista.append(x)
        winemag.insert_many(lista)
        



