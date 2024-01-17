#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastD = number % -(10)
        print(-(lastD), end='')
    else:
        lastD = number % 10
        print(lastD, end='')
    return abs(lastD)
