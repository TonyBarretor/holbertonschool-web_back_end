#!/usr/bin/env python3
"""Function that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Display various statistics for the given MongoDB collection"""
    # Count total logs
    total_logs = mongo_collection.count_documents({})

    # Display total logs
    print(f"{total_logs} logs")

    # Display methods count
    methods_count = {
        "GET": mongo_collection.count_documents({"method": "GET"}),
        "POST": mongo_collection.count_documents({"method": "POST"}),
        "PUT": mongo_collection.count_documents({"method": "PUT"}),
        "PATCH": mongo_collection.count_documents({"method": "PATCH"}),
        "DELETE": mongo_collection.count_documents({"method": "DELETE"}),
    }

    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")

    # Display status check count
    status_check_count = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

    # Display top 10 IPs
    top_ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Call the updated log_stats function
    log_stats(nginx_collection)
