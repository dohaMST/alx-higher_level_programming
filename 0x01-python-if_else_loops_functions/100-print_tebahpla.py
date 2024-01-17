#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        x = 0
    else:
        x = 32
    print('{}'.format(chr(i - x)), end='')
