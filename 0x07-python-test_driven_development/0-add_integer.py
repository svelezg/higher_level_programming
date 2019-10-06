#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """My addition function
    Args:  a: first integer b: second integer
    Returns:  The return value. a + b """
    if (a is None or (not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
