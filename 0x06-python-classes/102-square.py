#!/usr/bin/python3
class Square:
    """defines a square"""

    def __init__(self, size=0):
        """ This is the constructor function"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it """
        if (not isinstance(value, int) and not isinstance(value, float)):
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        return (self.size < other.size)

    def __gt__(self, other):
        return (self.area() > other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())

    def __eq__(self, other):
        return (self.size == other.size)

    def __eq__(self, other):
        return (self.area() == other.area())

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
