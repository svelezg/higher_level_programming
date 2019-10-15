#!/usr/bin/python3
"""
This is the "100-my_int" module.
The 100-my_int supplies one class, Myint.
"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __init__(self, a):
        """constructor"""
        self.__a = a

    def __eq__(self, other):
        """behavior for the equality operator, ==."""
        return (self.__a != other)

    def __ne__(self, other):
        """behavior for the inequality operator, !="""
        return (self.__a == other)
