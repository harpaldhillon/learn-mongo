import unittest
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

class MongoDBIndexCreator:
    def __init__(self, db_url, db_name, collection_name, index_field):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.index_field = index_field

    def create_unique_index(self):
        try:
            self.collection.create_index([(self.index_field, 1)], unique=True)
            print(f"Unique index created on field '{self.index_field}'")
        except Exception as e:
            print(f"Error creating unique index: {e}")
