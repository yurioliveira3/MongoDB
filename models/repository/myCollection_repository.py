from bson.objectid import ObjectId
from typing import Dict, List

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
        
        #for d in data:
        #    print(d)

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