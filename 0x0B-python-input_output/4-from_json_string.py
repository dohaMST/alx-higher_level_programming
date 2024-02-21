#!/usr/bin/python3
"""defining the function"""
import json


def from_json_string(my_str):
    """representing the function"""
    data = json.loads(my_str)
    return data
