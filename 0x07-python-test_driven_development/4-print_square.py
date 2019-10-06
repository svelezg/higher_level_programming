#!/usr/bin/python3
"""
This is the "4-print_square" module.

The 4-print_square module supplies one function, print_square(size).
"""


def print_square(size):
    """print_square function
    Args:  size is the size length of the square
    Prints:  a square """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    str = ""
    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                str += '#'
            str += '\n'
        print(str[:-1])
