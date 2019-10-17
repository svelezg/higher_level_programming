#!/usr/bin/python3
"""
This is the "100-append_after" module.
It supplies one function, append_after.
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
    a specific string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        new_text = ""
        for line in f:
            new_text += line
            if (search_string in line):
                new_text += new_string

    with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_text)
