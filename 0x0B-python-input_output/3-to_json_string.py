#!/usr/bin/python3
"""defining the function"""
import json


def to_json_string(my_obj):
    """representing the function"""
    data = json.dumps(my_obj)
    return data
