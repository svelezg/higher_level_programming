#!/usr/bin/python3
class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2 or
            not isinstance(position[0], int) or
                not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
                raise TypeError("position must be a " +
                                "tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
                raise TypeError("position must be a " +
                                "tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area method definition"""
        return self.__size ** 2

    def my_print(self):
        """my_print method definition"""
        if self.__size <= 0:
            print()
        else:
            for i in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
