#!/usr/bin/python3
"""
This is the "4-append_write" module.
It supplies one function, append_write.
"""


def append_write(filename="", text=""):
    """append_write function"""

    with open(filename, 'a') as f:
        return f.write(text)
