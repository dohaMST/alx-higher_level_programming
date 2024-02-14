#!/usr/bin/python3
"""Defining function."""


def matrix_mul(m_a, m_b):
    """a function that Multiplies two matrices.

    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_L = []
    for a in range(len(m_b[0])):
        newR = []
        for b in range(len(m_b)):
            newR.append(m_b[b][a])
        new_L.append(newR)

    new_matrix = []
    for r in m_a:
        newR = []
        for c in new_L:
            prod = 0
            for i in range(len(new_L[0])):
                prod += r[i] * c[i]
            newR.append(prod)
        new_matrix.append(newR)

    return new_matrix
