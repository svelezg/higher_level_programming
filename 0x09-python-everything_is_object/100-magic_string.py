#!/usr/bin/python3
class magic_string:
    """magic_string class"""

    number_of_instances = 0

    def __init__(self):
        """constructor"""
        magic_string.number_of_instances += 1

    def __str__(self):
        """end user output"""
        string = ""
        for i in range(0, magic_string.number_of_instances - 1):
            string = string + "Holberton, "
        string = string + "Holberton"
        return string
