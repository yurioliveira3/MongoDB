from models.connection_options.connection import DBConnectionHandler
from models.repository.myCollection_repository import myCollectionRepository

db_handle = DBConnectionHandler()
#conn1 = db_handle.get_db_connection()
#print(conn1)

db_handle.connect_to_db()

#db_handle.connect_to_db()
#conn2 = db_handle.get_db_connection()
#print(conn2)

db_connection = db_handle.get_db_connection()

# collection = conn2.get_collection("myCollection")
# collection.insert_one({
#     "Estou": "Inserindo novamente",
#     "Numeros": [123, 456, 789]
# })

#New instance of myCollection
myCollectionRepository = myCollectionRepository(db_connection)

# order = {
#     "name": "Yuri",
#     "endereco": "Cidade Enc",
#     "pedidos": {
#         "Pizza": "1",
#         "Refri": "2",
#         "Batata": "1"
#     }
# }

order = {
    "name": "Yuri",
    "surname": "Alves",
    "pedidos": {
        "Xis": 5
    }
}

myCollectionRepository.insert_document(order)

list_of_documents = [
    {"eric": "cartman"},
    {"stan": "march"},
    {"kenny": "mcCormick"},
    {"kyle": "Broflovski"}
]

myCollectionRepository.insert_list_of_documents(list_of_documents)
