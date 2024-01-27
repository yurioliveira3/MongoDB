from pymongo import MongoClient

#Define connection string
connection_string = "mongodb://root:root@0.0.0.0:27017/?authSource=admin"

#Instance Mongo Cli
client = MongoClient(connection_string)

#Define DB
db_connection = client["myDB"]

#Define Collection
collection = db_connection.get_collection("myCollection")

#Filter to find doc
search_filter = { "ola": "mundo" }

#Get Response
response = collection.find(search_filter)

for registry in response: print(registry) #Print Result

#Insert Object
collection.insert_one({
    "Estou": "Inserindo",
    "Numeros": [123, 456, 789]
})