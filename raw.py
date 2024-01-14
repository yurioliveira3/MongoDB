from pymongo import MongoClient

connection_string = "mongodb://root:root@0.0.0.0:27017/?authSource=admin"

client = MongoClient(connection_string)

db_connection = client["myDB"]

print(db_connection)

collection = db_connection.get_collection("myCollection")

print(collection)

search_filter = { "ola": "mundo" }

response = collection.find(search_filter)

#print(response)

for registry in response: print(registry)

collection.insert_one({
    "Estou": "Inserindo",
    "Numeros": [123, 456, 789]
})