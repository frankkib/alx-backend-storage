#!/usr/bin/env python3
"""
101-students module

This module contains functions to interact with MongoDB collections
related to students,
including calculating and sorting students by their average scores.
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by average score from highest to lowest.
    Each student includes their average score with key "averageScore".
    """
    pipeline = [{
        '$addFields': {
            'averageScore': {
                '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
                }
            },
        {
            '$project': {
                'name': 1,
                'averageScore': 1
                }
            }
        ]
    return list(mongo_collection.aggregate(pipeline))
