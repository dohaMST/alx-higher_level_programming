#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    arr = matrix.copy()
    for i in range(len(matrix)):
        arr[i] = list(map(lambda x: x**2, matrix[i]))
    return (arr)
