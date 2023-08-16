#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """returns all the documents"""
    documents = list(mongo_collection.find())
    return documents
