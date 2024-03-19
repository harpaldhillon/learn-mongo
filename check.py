from pymongo import MongoClient

def check_record_exists(collection, query):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    collection = db[collection]

    # Check if record exists
    if collection.find_one(query):
        return True
    else:
        return False

# Example usage:
if __name__ == "__main__":
    collection_name = 'mycollection'
    query = {'name': 'John Doe'}  # Example query to find a record with name 'John Doe'
    if check_record_exists(collection_name, query):
        print("Record exists in MongoDB")
    else:
        print("Record does not exist in MongoDB")

