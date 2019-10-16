#!/usr/bin/python3


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__
