#!/usr/bin/python3
"""
This is the "8-rectangle" module.
The 8-rectangle module supplies one class, Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module"""


class Rectangle(BaseGeometry):
    """Rectangle class based upon BaseGeometry"""

    def __init__(self, width, height):
        """constructor"""
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height
