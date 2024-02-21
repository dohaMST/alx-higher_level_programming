#!/usr/bin/python3
"""defining the function"""
import json


def save_to_json_file(my_obj, filename):
    """representing the function"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
