from bson.objectid import ObjectId
from typing import Dict, List
from datetime import timedelta
class myCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "myCollection"
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)  
        return document

    def insert_list_of_documents(self, list_of_documents: List[Dict]) ->  List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)  
        return list_of_documents
    
    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, { "_id" : 0 })
        return response

    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        #data = collection.find({})
        #data = collection.find({"name": "Yuri"})
        data = collection.find(
            #{"name" : "Yuri", "pedidos.Pizza" : "1"}, #filter example
            filter,
            {"_id" : 0, "endereco" : 0} #return options, #removing id and endereco columns
            )
        
        response = []
        for elem in data: response.append(elem)

        return response
    
    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            {"name" : "Yuri"}, #filter
            {"_id" : 0, "endereco" : 0} #return options, #removing id and endereco columns
        ).sort([("pedidos.Xis", -1)])
        
        for elem in data: print(elem)
        
    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "surname" : { "$exists": True } })
        for elem in data: print(elem)

    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "$or" : [ {"name" : "Yuri"}, {"ola" : { "$exists" : True}} ] })
        for elem in data: print(elem)

    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"_id" : ObjectId("65a44105aaf3e3885fcda051") })
        for elem in data: print(elem)

    def edit_registry(self, name) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one(
            { "_id": ObjectId("65b23e67eae50856a63ea68a") }, #filter
            #{ "$set": {"name" : "Yuri Oliveira"} }
            { "$set": {"name" : name} }
        )
        print(data.modified_count)

    def edit_many_registers(self, filter, properties) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            filter,
            { "$set": properties }
        )
        print(data.modified_count)

    def edit_many_increment(self, num) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            { "_id": ObjectId("65b23e67eae50856a63ea68a") }, #filter
            { "$inc": { "age" : num }}
        )
        print(data.modified_count)

    def delete_many_registers(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many( { "role" : "DBA" } )
        print(data.deleted_count)

    def delete_one_register(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one( { "role" : "DBA" } )
        print(data.deleted_count)

    def create_index_ttl(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        life_time = timedelta(seconds=9)
        collection.create_index("created", expireAfterSeconds=life_time.seconds)