#!/usr/bin/env python3
"""function that add new document into a collection"""


def insert_school(mongo_collection, **kwargs):
    """returns the new id added"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
