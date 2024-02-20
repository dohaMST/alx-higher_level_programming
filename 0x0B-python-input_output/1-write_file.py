#!/usr/bin/python3
"""defining the function"""


def write_file(filename="", text=""):
    """representing the function"""

    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
