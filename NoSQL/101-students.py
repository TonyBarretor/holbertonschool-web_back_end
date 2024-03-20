#!/usr/bin/env python3

"""Function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    Return all students sorted by average score.
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]

    top_students = list(mongo_collection.aggregate(pipeline))
    for student in top_students:
        student["_id"] = str(student["_id"])  # Convert ObjectId to string

    return top_students
