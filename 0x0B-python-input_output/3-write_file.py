#!/usr/bin/python3
"""
This is the "3-write_file" module.
It supplies one function, write_file.
"""


def write_file(filename="", text=""):
    """write_file function"""

    with open(filename, 'w') as f:
        return f.write(text)
