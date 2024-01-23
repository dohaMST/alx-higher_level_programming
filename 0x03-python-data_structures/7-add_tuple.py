#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    size_a, size_b = len(tuple_a), len(tuple_b)
    tupX = ((tuple_a[0] if size_a >= 1 else 0) +
                 (tuple_b[0] if size_b >= 1 else 0),
                 (tuple_a[1] if size_a >= 2 else 0) +
                 (tuple_b[1] if size_b >= 2 else 0))
    return tupX
