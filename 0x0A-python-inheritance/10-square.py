#!/usr/bin/python3
"""
This is the "10-square" module.
The 10-square module supplies one module, Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based upon Rectangle"""

    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
