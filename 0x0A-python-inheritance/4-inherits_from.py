#!/usr/bin/python3
"""
This is the "4-inherits_from" module.
The 4-inherits_from module supplies one function, inherits_from.
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified
    class ; otherwise False."""
    return isinstance(obj, a_class) and not type(obj) == a_class
