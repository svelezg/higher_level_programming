#!/usr/bin/python3
"""
This is the "5-to_json_string" module.
It supplies one function, to_json_string.
"""


import json


def to_json_string(my_obj):
    """to_json_string function"""

    return json.dumps(my_obj)
