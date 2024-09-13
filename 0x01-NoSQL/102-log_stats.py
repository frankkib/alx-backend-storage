#!/usr/bin/env python3
"""Script to provide statistics about Nginx logs stored in MongoDB, including top 10 most frequent IPs"""

from pymongo import MongoClient
from pymongo import DESCENDING

def log_stats(mongo_collection):
    total_logs = mongo_collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}

    get_status_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    print(f"\tGET /status: {get_status_count}")

    pipeline = [
        {
            '$group': {
                '_id': '$ip',
                'count': { '$sum': 1 }
            }
        },
        {
            '$sort': {
                'count': DESCENDING
            }
        },
        {
            '$limit': 10
        }
    ]
    
    ip_counts = mongo_collection.aggregate(pipeline)
    
    print("Top 10 most frequent IPs:")
    for ip_doc in ip_counts:
        print(f"\t{ip_doc['_id']}: {ip_doc['count']}")

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']
    
    log_stats(collection)
