import boto3
import json
import time
from uuid import uuid4

s3 = boto3.client('s3')
bucket_name = 'harpaldhillon123'
prefix = 'test-cache/'

# Step 1: Upload 1000 small JSON files
print("Uploading files...")
for i in range(1000):
    data = {"id": i, "uuid": str(uuid4()), "value": f"some random value {i}"}
    key = f"{prefix}file_{i}.json"
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data), ContentType='application/json')
print("Upload complete.")

# Step 2: Read each file and measure time taken
print("\nReading files...")
read_times = []

for i in range(1000):
    key = f"{prefix}file_{i}.json"
    start = time.time()
    response = s3.get_object(Bucket=bucket_name, Key=key)
    content = response['Body'].read()
    elapsed = time.time() - start
    read_times.append(elapsed)
    print(f"File {i}: {elapsed:.4f} seconds")

# Summary
average_time = sum(read_times) / len(read_times)
print(f"\nAverage read time: {average_time:.4f} seconds")

