# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, user, passwd): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = user 
        PASS = passwd 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        # I added a read check to prevent exact duplicates 
        if data is not None and ((len(list(self.read(data)))) < 1):
            result = self.database.animals.insert_one(data)  # data should be dictionary
            return result.acknowledged
        else:
            raise Exception("Either data is empty or record already exists.") 

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            results = self.database.animals.find(query)
            return list(results)
        else:
            raise Exception("Error: query parameter empty")
            
    def update(self, query, new_data):
        if new_data is not None and query is not None:
            result = self.database.animals.update_many(query, { "$set": new_data })
            return result.modified_count
        else:
            raise Exception("Error: missing query or new values")
    
    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Error: query empty")
            