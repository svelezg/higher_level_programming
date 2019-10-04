#!/usr/bin/python3
"""
This is the "3-say_my_name" module.

The 3-say_my_name.py module supplies one function, say_my_name"").
"""


def say_my_name(first_name, last_name=""):
    """Say my name function function
    Args:  first_name last_name
    Returns:  My name """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
