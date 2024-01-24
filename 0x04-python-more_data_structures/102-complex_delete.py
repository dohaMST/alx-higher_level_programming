#!/usr/bin/python3
def complex_delete(my_dict, value):
    arr = my_dict.copy()
    for i, j in arr.items():
        if value == j:
            my_dict.pop(i)
    return my_dict
