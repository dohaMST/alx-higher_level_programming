#!/usr/bin/python3
"""defining the function"""


def append_write(filename="", text=""):
    """representing the function"""

    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
