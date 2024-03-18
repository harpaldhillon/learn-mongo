import pymongo

class MongoDBClient:
    def __init__(self, host='192.168.1.214', port=27017, db_name='test', collection_name='data'):
        # self.client = pymongo.MongoClient(host, port)
        self.client = pymongo.MongoClient("mongodb://admin:pass@192.168.1.214:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_record(self, record):
        try:
            result = self.collection.insert_one(record)
            print("Record Acknowledged:", result.acknowledged)
            print("Record inserted successfully. Inserted ID:", result.inserted_id)
        except Exception as e:
            print("Error inserting record:", e)

    def update_record(self, filter_criteria, update_data):
        try:
            result = self.collection.update_one(filter_criteria, {"$set": update_data})
            print("Record updated successfully. Matched Count:", result.matched_count)
        except Exception as e:
            print("Error updating record:", e)

    def close_connection(self):
        self.client.close()

# Example usage:
if __name__ == "__main__":
    # Create an instance of MongoDBClient
    mongo_client = MongoDBClient(host='localhost', port=27017, db_name='test', collection_name='data')

    # Insert a record
    record_to_insert = {"name": "John", "age": 30, "city": "New York"}
    mongo_client.insert_record(record_to_insert)

    # Update a record
    filter_criteria = {"name": "John"}
    update_data = {"age": 35}
    mongo_client.update_record(filter_criteria, update_data)

    # Close the connection
    mongo_client.close_connection()
