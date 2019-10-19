#!/usr/bin/python3
"""
This is the "base" module.
It supplies one class, base.
"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
