#!/usr/bin/python3
"""
This is the "7-save_to_json" module.
It supplies one function, save_to_json_file.
"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function"""

    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
