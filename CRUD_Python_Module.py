
from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 

        # Connection Variables 
        # 
        USER = username 
        PASS = password
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
        if data is not None: 
            try:
                self.database.animals.insert_one(data) # data should be dictionary             
                return True
            except Exception as e:
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                results = list(self.database.animals.find(query))
                return results
            except Exception as e:
                return []
        else:
            return []
        
    #Create method to implement the U in CRUD.
    def update(self, query, update_data):
        if query is not None:
            try:
                result = self.database.animals.update_many(query, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                return 0
        else: 
            return 0
        
    def delete(self, query):
        if query is not None:
            try:
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            except Exception as e:
                return 0
        else:
            return 0
       