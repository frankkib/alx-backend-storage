#!/usr/bin/env python3
"""function that returns the list of school having a specific
topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of topics"""
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
