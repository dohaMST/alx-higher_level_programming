#!/usr/bin/python3


def text_indentation(text=None):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    k = 0
    while k < len(text) and text[k] == ' ':
        k += 1

    while k < len(text):
        print(text[k], end="")
        if text[k] == "\n" or text[k] in ".?:":
            if text[k] in ".?:":
                print("\n")
            k += 1
            while k < len(text) and text[k] == ' ':
                k += 1
            continue
        k += 1
