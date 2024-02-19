#!/usr/bin/python3
""" checks if obj is  sub class of a class """


def inherits_from(obj, a_class):
    """returns true or false"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
