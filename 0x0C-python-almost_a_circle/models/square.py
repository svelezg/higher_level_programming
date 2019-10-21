#!/usr/bin/python3
"""
This is the "square module.
It supplies one class, square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    __nb_objects = 0

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """end user output"""
        return ("[Square] " + "(" + str(self.id) + ") " +
                str(self.x) + "/" + str(self.y) + " - " +
                str(self.size))

    @property
    def size(self):
        """getter for width"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        var = ['id', 'size', 'x', 'y']
        if len(args) != 0 and args[0] is not "":
            for i in range(len(args)):
                setattr(self, var[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """"returns the dictionary representation of a Square"""
        attributes = ["id", "size", "x", "y"]
        values = [self.id, self.size, self.x, self.y]
        return dict(zip(attributes, values))
