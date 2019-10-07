#!/usr/bin/python3
class Rectangle:
    """empty Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

    def area(self):
        """area method definition"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method definition"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """end user output"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (
                    (self.__height - 1) *
                    (self.__width * str(self.print_symbol) + "\n") +
                    self.__width * str(self.print_symbol))

    def __repr__(self):
        """object reproduction"""
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """"delete magic method"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
