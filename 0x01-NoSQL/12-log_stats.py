#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def print_nginx_log_stats():
    """Print statistics about the Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']
    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}
    get_status_count = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    print(f"\tGET /status: {get_status_count}")


if __name__ == "__main__":
    print_nginx_log_stats()
