#!/usr/bin/python3
""" function that returns if the obj is class or inherit from a class"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
