#!/usr/bin/env python3
"""function that cahnges all topics in documents"""


def update_topics(mongo_collection, name, topics):
    """returns the new object"""
    result = mongo_collection.update_one(
            {"name": name},
            {"$set": {"topics": topics}}
            )
    if result.modified_count > :
        return "OK"
    else:
        return "No documets updated"
