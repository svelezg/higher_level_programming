#!/usr/bin/python3
"""
This is the "11.square" module.
The 11-sqaure module supplies one class, Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based upon Rectangle"""

    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """end user output"""
        return (
                    "[Square] " +
                    str(self.__size) + "/" + str(self.__size))
