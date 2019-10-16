#!/usr/bin/python3
"""
This is the "6-from_json_string" module.
It supplies one function, from_json_string.
"""

import json


def from_json_string(my_str):
    """from_json_string function"""

    return json.loads(my_str)
