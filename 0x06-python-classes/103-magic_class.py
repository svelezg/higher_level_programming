#!/usr/bin/python3
# import dis
import math


class MagicClass:
    """defines a circle"""

    def __init__(self, radius=0):
        self.radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius

# dis.dis(MagicClass)
