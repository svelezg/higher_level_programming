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

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        "compares areas"
        if((self.__size ** 2) < (other.__size ** 2)):
            return True

    def __gt__(self, other):
        "compares areas"
        if(self.area() > other.area()):
            return True

    def __le__(self, other):
        "compares areas"
        if(self.area() <= other.area()):
            return True

    def __ge__(self, other):
        "compares areas"
        if(self.area() >= other.area()):
            return True

    def __eq__(self, other):
        "compares areas"
        if(self.area() == other.area()):
            return True

    def __eq__(self, other):
        "compares areas"
        if(self.area() != other.area()):
            return True
