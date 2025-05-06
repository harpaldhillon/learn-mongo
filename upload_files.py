import boto3
import time
import os
import uuid
from pathlib import Path
import json

# Configuration
BUCKET_NAME = 'harpaldhillon12345'
NUM_FILES = 1000
LOCAL_DIR = Path('./temp_files_for_upload_json')

# Create test files
def create_test_files():
    LOCAL_DIR.mkdir(exist_ok=True)
    data = {
        "users": [
        {
           "id": 1,
           "name": "Alice",
           "email": "alice@example.com",
           "active": "true"
        },
        {
           "id": 2,
           "name": "Bob",
           "email": "bob@example.com",
           "active": "false"
        }
      ]
    }

    for i in range(NUM_FILES):
        with open(LOCAL_DIR/f"user_{i}.json", "w") as f:
            json.dump(data, f, indent=4)

# Upload to S3
def upload_files_to_s3():
    s3 = boto3.client('s3')
    start = time.time()
    
    for i in range(NUM_FILES):
        file_path = LOCAL_DIR / f"user_{i}.json"
        s3_key = f"test_uploads/{uuid.uuid4()}.txt"
        s3.upload_file(str(file_path), BUCKET_NAME, s3_key)
    
    end = time.time()
    print(f"Uploaded {NUM_FILES} files in {end - start:.2f} seconds")
    print(f"Average time per file: {(end - start)/NUM_FILES:.4f} seconds")

if __name__ == "__main__":
    print("Creating test files...")
    create_test_files()
    print("Uploading files to S3...")
    upload_files_to_s3()

