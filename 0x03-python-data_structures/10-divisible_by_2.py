#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    if my_list:
        for num in my_list:
            list2.append(False if num % 2 else True)
        return list2
