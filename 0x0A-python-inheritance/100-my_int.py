#!/usr/bin/python3
"""defining the class"""


class MyInt(int):
    """representing the class"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
