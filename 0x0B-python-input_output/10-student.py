#!/usr/bin/python3
"""defining the class"""


class Student:
    """representing the class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return (self.__dict__)
        x = dict()
        for i in attrs:
            for j in self.__dict__:
                if (i == j):
                    x[i] = self.__dict__[j]
        return (x)
