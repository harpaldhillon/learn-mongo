import unittest
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
        # Connect to a test database
        self.test_client = MongoClient('mongodb://localhost:27017/')
        self.test_db = self.test_client['test_database']
        self.test_collection = self.test_db['test_collection']

    def test_index_creation(self):
        # Create MongoDBCompoundIndexCreator instance
        index_creator = MongoDBCompoundIndexCreator('mongodb://localhost:27017/', 'test_database', 'test_collection', ['field1', 'field2'])
        # Create compound index
        index_creator.create_compound_index()
        # Check if index was created
        indexes = self.test_collection.index_information()
        self.assertIn('field1_1_field2_1', indexes)
        self.assertFalse(indexes['field1_1_field2_1']['unique'])

    def test_duplicate_insertion(self):
        # Create MongoDBCompoundIndexCreator instance
        index_creator = MongoDBCompoundIndexCreator('mongodb://localhost:27017/', 'test_database', 'test_collection', ['field1', 'field2'])
        # Create compound index
        index_creator.create_compound_index()
        # Insert a document with duplicate values
        self.test_collection.insert_one({'field1': 'value1', 'field2': 'value2'})
        with self.assertRaises(DuplicateKeyError):
            # Attempt to insert another document with the same values
            self.test_collection.insert_one({'field1': 'value1', 'field2': 'value2'})

    def tearDown(self):
        # Drop the test collection
        self.test_db.drop_collection('test_collection')
        # Close the test client
        self.test_client.close()

if __name__ == '__main__':
    unittest.main()

