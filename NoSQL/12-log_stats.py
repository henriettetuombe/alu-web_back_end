#!/usr/bin/env python3
from pymongo import MongoClient

def log_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs  # Database name: logs
    collection = db.nginx  # Collection name: nginx

    # 1. Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Print the number of logs by HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Count GET requests to the `/status` path
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Close the MongoDB connection
    client.close()

if __name__ == "__main__":
    log_stats()
