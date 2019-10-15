#!/usr/bin/python3
"""
This is the "3-is_kind_of_class" module.
The 3-is_kind_of_class module supplies one function, is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise False."""
    return issubclass(type(obj), a_class)
