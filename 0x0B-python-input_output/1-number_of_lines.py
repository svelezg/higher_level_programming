#!/usr/bin/python3
"""
This is the "1-number_of_lines" module.
It supplies one function, number_of_lines.
"""


def number_of_lines(filename=""):
    """number_of_lines function"""

    counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            counter += 1

    return counter
