from pymongo import MongoClient
from pymongo.errors import PyMongoError
import unittest
from unittest.mock import MagicMock

class MongoDB:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)

    def read_all_documents(self, database_name, collection_name):
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            return list(collection.find())
        except PyMongoError as e:
            print(f"Error reading documents: {e}")
            return []

class TestMongoDB(unittest.TestCase):
    def setUp(self):
        # Create a mock MongoClient instance
        self.mock_client = MagicMock()

        # Patch MongoClient to return the mock client
        self.patcher = unittest.mock.patch('pymongo.MongoClient', return_value=self.mock_client)
        self.patcher.start()

        # Create an instance of MongoDB class
        self.db = MongoDB('mock_connection_string')

    def tearDown(self):
        # Stop the patcher
        self.patcher.stop()

    def test_read_all_documents_success(self):
        # Mock find() method of the collection
        self.mock_client.test_database.test_collection.find.return_value = [{'_id': 1, 'name': 'Alice'}, {'_id': 2, 'name': 'Bob'}]

        # Call the read_all_documents method
        documents = self.db.read_all_documents('test_database', 'test_collection')

        # Assert that the method returns the expected result
        self.assertEqual(documents, [{'_id': 1, 'name': 'Alice'}, {'_id': 2, 'name': 'Bob'}])

    def test_read_all_documents_failure(self):
        # Mock find() method of the collection to raise PyMongoError
        self.mock_client.test_database.test_collection.find.side_effect = PyMongoError('Read error')

        # Call the read_all_documents method
        documents = self.db.read_all_documents('test_database', 'test_collection')

        # Assert that the method returns an empty list indicating failure
        self.assertEqual(documents, [])

if __name__ == '__main__':
    unittest.main()

