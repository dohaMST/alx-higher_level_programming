#!/usr/bin/python3
"""defining the function"""


def pascal_triangle(n):
    """rpresenting the function"""

    if n <= 0:
        return []

    lst = [[1], [1, 1]]
    for i in range(2, n):
        listR = []
        listR.append(1)
        listR.append(1)
        for j in range(1, i):
            listR.insert(j, lst[i - 1][j] + lst[i - 1][j - 1])
        lst.append(listR)
    return lst[:n]
