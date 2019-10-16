#!/usr/bin/python3
"""
This is the "0-read" module.
It supplies one function, read_file.
"""


def read_file(filename=""):
    """read_file function"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
