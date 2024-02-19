#!/usr/bin/python3
"""defining MyList calss"""


class MyList(list):
    """class 'MyList' inherits from 'list' """

    def print_sorted(self):
        print(sorted(self))
