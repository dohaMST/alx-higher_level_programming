#!/usr/bin/python3
"""defining the function"""


def append_after(filename="", search_string="", new_string=""):
    """representing the function"""
    data = ""
    with open(filename) as fr:
        for line in fr:
            data += line
            if search_string in line:
                data += new_string
    with open(filename, "w") as fw:
        fw.write(data)
