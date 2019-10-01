#!/usr/bin/python3
class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area method definition"""
        return self.__size ** 2

    def my_print(self):
        """my_print method definition"""
        if self.__size <= 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
