#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for x in matrix:
        arr.append([i**2 for i in x])
    return arr

