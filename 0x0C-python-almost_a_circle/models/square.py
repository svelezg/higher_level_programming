#!/usr/bin/python3
"""
This is the "square module.
It supplies one class, square.
"""


class Square(Rectangle):
    """Rectangle class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
