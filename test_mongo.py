import unittest
from unittest.mock import MagicMock
from mymodule import MyMongoDBClass  # Import the class that interacts with MongoDB

class TestMongoDB(unittest.TestCase):
    def setUp(self):
        # Create a mock MongoClient instance
        self.mock_client = MagicMock()

        # Create a mock database and collection
        self.mock_db = self.mock_client['test_database']
        self.mock_collection = self.mock_db['test_collection']

        # Patch MongoClient to return the mock client
        self.patcher = unittest.mock.patch('mymodule.MongoClient', return_value=self.mock_client)
        self.patcher.start()

        # Create an instance of MyMongoDBClass
        self.db = MyMongoDBClass()

    def tearDown(self):
        # Stop the patcher
        self.patcher.stop()

    def test_create_document(self):
        # Mock insert_one method of the collection
        self.mock_collection.insert_one.return_value.inserted_id = '123'

        # Call the method to be tested
        result = self.db.create_document('test_collection', {'key': 'value'})

        # Assert that the method returns the expected result
        self.assertEqual(result, '123')

    # Similarly, you can write tests for other CRUD operations

if __name__ == '__main__':
    unittest.main()

