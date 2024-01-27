from models.connection_options.connection import DBConnectionHandler
from models.repository.myCollection_repository import myCollectionRepository
from datetime import datetime, timedelta

#Instance mongo Handler
db_handle = DBConnectionHandler()
#Get the DB connection
conn1 = db_handle.get_db_connection()
#Instance MongoClient and connect to DB
db_handle.connect_to_db()

db_connection = db_handle.get_db_connection()

# Exemplifying - Create another connection (conn2)
#conn2 = db_handle.get_db_connection()
#print(conn2)
# collection = conn2.get_collection("myCollection")
# collection.insert_one({
#     "Iam": "Insert Again",
#     "numbers": [123, 456, 789]
# })

#New instance of myCollection
myCollectionRepository = myCollectionRepository(db_connection)

#Define orders to insert
order_1 = {
    "name": "Yuri",
    "addr": "Cidade Enc",
    "order": {
        "Pizza": "1",
        "Refri": "2",
        "Batata": "1"
    }
}

order_2 = {
    "name": "Yuri",
    "surname": "Barros",
    "order": {
        "Xis": 5
    }
}

#Insert new doc in collection [ONE BY ONE]
myCollectionRepository.insert_document(order_1)
myCollectionRepository.insert_document(order_2)

#Define a list of orders to insert LIST[DICT]
orders = [
    {
        "name": "João",
        "addr": "Centro",
        "order": {
            "Batata": "3",
            "Refri": "1"
        }
    },
    {
        "name": "Maria",
        "surname": "Joaquina",
        "order": {
            "Xis": 10
        }
    },
    {
        "name": "Simone",
        "surname": "Melo",
        "order": {
            "Xis": 5
        }
    }
]

#Insert new doc in collection [LIST]
myCollectionRepository.insert_list_of_documents(orders)

#Select one or more docs 
response = myCollectionRepository.select_many({"name" : "Yuri"})
print(response)

#Get only the first returned doc
response2 = myCollectionRepository.select_one({"name" : "Yuri"}) 
print(response2)

#Select all docs with a certain propertie
myCollectionRepository.select_if_property_exists()

#Return only the orders without _id and addr
myCollectionRepository.select_many_order()

#Select with OR options 
myCollectionRepository.select_or()

#Select a specific doc, using the "_id"
myCollectionRepository.select_by_object_id()

#New list with the role propertie
new_list_of_documents = [
    {
        "name": "Yuri", 
        "nickname": "Yu3",
        "role": "DBA"
    },
    {
        "name": "Paulo", 
        "nickname": "Ptb", 
        "role": "Data Enginner"
    }
]

#Insert the new list
myCollectionRepository.insert_list_of_documents(new_list_of_documents)

#Edit a register, change the name -> "$set": {"name"} 
myCollectionRepository.edit_registry("Yuri Oliveira")

#Edit all the registers, change role to Data Architect - Example
#myCollectionRepository.edit_many_registers("Data Architect")

#Create a filter to edit docs
filter = { "role" : "DBA" }
properties = { "role" : "Data Architect" }

#Change role DBA -> Data Architect
myCollectionRepository.edit_many_registers(filter, properties)

#Add addr propertie if not exists in doc
filter_2 = { "name" : "Yuri" }
properties_2 = { "addr" : {
                "cep" : "98170-000",
                "street" : "Centro",
                "city" :  "Tupancireta"
            } }

#Do the "update"
myCollectionRepository.edit_many_registers(filter_2, properties_2)

#Increment a certain propertie, in the case we add 1 year to "age"
myCollectionRepository.edit_many_increment(1)

#Do a delete in all of docs
myCollectionRepository.delete_many_registers()

#Do a delete in the one find
myCollectionRepository.delete_one_register()

#Create a TTL index in the created propertie
myCollectionRepository.create_index_ttl()

#Create a new doc with TTL index
idx_doc = { 
        "name": "Yuri", 
        "age": "50", 
        "created": datetime.utcnow() -timedelta(hours=3) 
    }

#Insert the doc... After 9 seconds the life_time expire and doc is deleted
myCollectionRepository.insert_document(idx_doc)