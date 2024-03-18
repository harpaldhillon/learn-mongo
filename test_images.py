# Unit tests
import unittest

from images import MongoDB

class TestMongoDB(unittest.TestCase):
    def setUp(self):
        self.db = MongoDB()

    def test_crud_operations(self):
        # Test create
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        document_id = self.db.create_document('users', data)
        self.assertIsNotNone(document_id)

        # Test read
        query = {'name': 'John'}
        document = self.db.read_document('users', query)
        self.assertIsNotNone(document)

        # Test update
        updated_data = {'age': 31}
        updated_count = self.db.update_document('users', query, updated_data)
        self.assertEqual(updated_count, 1)

        # Test delete
        deleted_count = self.db.delete_document('users', query)
        self.assertEqual(deleted_count, 1)

if __name__ == '__main__':
    unittest.main()