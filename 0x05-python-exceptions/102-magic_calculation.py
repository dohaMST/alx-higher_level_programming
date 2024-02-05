#!/usr/bin/python3

def magic_calculation(a, b):
    x = 0
    for t in range(1, 3):
        try:
            if t > a:
                raise Exception("Too far")
            else:
                x += a ** b / t
        except Exception:
            x = b + a
            break
    return x
