#!/usr/bin/python3
"""
This is the "101-add_attribute" module.
The 101-add_attribute module supplies one function, add_attribute.
"""


def add_attribute(object, attribute, value):
    """adds a new attribute to an object if its possible"""
    if hasattr(object, "__dict__"):
        setattr(object, attribute, value)
    else:
        raise TypeError("can't add new attribute")
