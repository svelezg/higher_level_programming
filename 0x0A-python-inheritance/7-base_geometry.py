#!/usr/bin/python3
"""
This is the "7-base_geometry" module.
The 7-base_geometry module supplies one function, base_geometry.
"""


class BaseGeometry:
    """empty class BaseGeometry"""

    def area(self):
        """raises an exeption"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
