import pymongo
from pymongo import MongoClient

class MongoDB:
    def __init__(self, host='localhost', port=27017, db_name='test1'):
        # self.client = MongoClient(host, port)
        self.client = pymongo.MongoClient("mongodb://admin:pass@192.168.1.214:27017/")
        self.db = self.client[db_name]

    def create_document(self, collection_name, data):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(data)
            return result.inserted_id
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return None

    def read_document(self, collection_name, query):
        try:
            collection = self.db[collection_name]
            document = collection.find_one(query)
            return document
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return None

    def update_document(self, collection_name, query, data):
        try:
            collection = self.db[collection_name]
            result = collection.update_one(query, {"$set": data})
            return result.modified_count
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return None

    def delete_document(self, collection_name, query):
        try:
            collection = self.db[collection_name]
            result = collection.delete_one(query)
            return result.deleted_count
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return None
        
    def close_connection(self):
        self.client.close()

# Example usage:
if __name__ == "__main__":
    # Create an instance of MongoDBClient
    mongo_client = MongoDB(host='localhost', port=27017, db_name='test1')#, collection_name='data1')

    # Insert a record
    record_to_insert = {"name": "John", "age": 30, "city": "New York"}
    mongo_client.create_document('data1', record_to_insert)

    # Update a record
    filter_criteria = {"name": "John"}
    update_data = {"age": 35}
    mongo_client.update_document('data1',filter_criteria, update_data)

    # Get a record
    query_data = {"name": "John"}
    # update_data = {"age": 35}
    print(mongo_client.read_document('data1',query_data))


    # Close the connection
    mongo_client.close_connection()