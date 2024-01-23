#!/usr/bin/python3
def no_c(my_string):
    str2 = ""
    for elm in my_string:
        if elm != "c" and elm != "C":
            str2 += elm
    return str2
