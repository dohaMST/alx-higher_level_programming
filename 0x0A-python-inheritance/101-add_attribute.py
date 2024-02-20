#!/usr/bin/python3
"""defining the class"""


def add_attribute(obj, att, value):
    """representing the class"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
