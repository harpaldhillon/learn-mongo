import unittest
from unittest.mock import MagicMock
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

class MongoDBCompoundIndexCreator:
    def __init__(self, db_url, db_name, collection_name, index_fields):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.index_fields = index_fields

    def create_compound_index(self):
        try:
            self.collection.create_index([(field, 1) for field in self.index_fields])
            print(f"Compound index created on fields: {', '.join(self.index_fields)}")
        except Exception as e:
            print(f"Error creating compound index: {e}")

class TestMongoDBCompoundIndexCreator(unittest.TestCase):
    def setUp(self):
        # Mock the MongoClient and its attributes
        self.mock_client = MagicMock()
        self.mock_db = MagicMock()
        self.mock_collection = MagicMock()
        self.mock_client.__getitem__.return_value = self.mock_db
        self.mock_db.__getitem__.return_value = self.mock_collection

    def test_index_creation(self):
        # Create MongoDBCompoundIndexCreator instance
        index_creator = MongoDBCompoundIndexCreator('mongodb://localhost:27017/', 'test_database', 'test_collection', ['field1', 'field2'])
        index_creator.client = self.mock_client
        # Create compound index
        index_creator.create_compound_index()
        # Check if index was created
        self.mock_collection.create_index.assert_called_once_with([('field1', 1), ('field2', 1)])

    def test_duplicate_insertion(self):
        # Create MongoDBCompoundIndexCreator instance
        index_creator = MongoDBCompoundIndexCreator('mongodb://localhost:27017/', 'test_database', 'test_collection', ['field1', 'field2'])
        index_creator.client = self.mock_client
        # Mock create_index method to raise DuplicateKeyError
        self.mock_collection.create_index.side_effect = DuplicateKeyError("Duplicate key error")
        # Attempt to create compound index
        index_creator.create_compound_index()
        # Check if DuplicateKeyError is raised
        self.assertRaises(DuplicateKeyError, index_creator.create_compound_index)

if __name__ == '__main__':
    unittest.main()

