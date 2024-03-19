import unittest
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from index import MongoDBIndexCreator

class TestMongoDBIndexCreator(unittest.TestCase):
    def setUp(self):
        # Connect to a test database
        self.test_client = MongoClient('mongodb://localhost:27017/')
        self.test_db = self.test_client['test_database']
        self.test_collection = self.test_db['test_collection']

    def test_index_creation(self):
        # Create MongoDBIndexCreator instance
        index_creator = MongoDBIndexCreator('mongodb://localhost:27017/', 'test_database', 'test_collection', 'test_field')
        # Create unique index
        index_creator.create_unique_index()
        # Check if index was created
        indexes = self.test_collection.index_information()
        self.assertIn('test_field_1', indexes)
        self.assertTrue(indexes['test_field_1']['unique'])

    def test_duplicate_insertion(self):
        # Create MongoDBIndexCreator instance
        index_creator = MongoDBIndexCreator('mongodb://localhost:27017/', 'test_database', 'test_collection', 'test_field')
        # Create unique index
        index_creator.create_unique_index()
        # Insert a document with a duplicate value
        self.test_collection.insert_one({'test_field': 'value1'})
        with self.assertRaises(DuplicateKeyError):
            # Attempt to insert another document with the same value
            self.test_collection.insert_one({'test_field': 'value1'})

    def tearDown(self):
        # Drop the test collection
        self.test_db.drop_collection('test_collection')
        # Close the test client
        self.test_client.close()

if __name__ == '__main__':
    unittest.main()

