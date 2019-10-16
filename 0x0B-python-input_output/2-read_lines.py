#!/usr/bin/python3
"""
This is the "2-read_lines" module.
It supplies one function, read_lines.
"""


def read_lines(filename="", nb_lines=0):
    """read_lines function"""

    counter = 0

    with open(filename, encoding='utf-8') as f:
        for line in f:
            if ((nb_lines <= 0) or (counter < nb_lines)):
                print(line, end="")
                counter += 1
