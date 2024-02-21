#!/usr/bin/python3
"""defining the function"""
import json


def load_from_json_file(filename):
    """representing the function"""
    with open(filename, 'r') as f:
        return json.load(f)
