#!/usr/bin/python3
"""
This is the "9-rectangle" module.
The 9-rectangle module supplies one class, Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based upon BaseGeometry"""

    def __init__(self, width, height):
        """constructor"""
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method definition"""
        return self.__width * self.__height

    def __str__(self):
        """end user output"""
        return (
                "[Rectangle] " + str(self.__width) + "/" + str(self.__height))
