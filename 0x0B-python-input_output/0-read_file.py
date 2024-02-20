#!/usr/bin/python3
"""defining a function"""


def read_file(filename=""):
    """representing the function"""
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
