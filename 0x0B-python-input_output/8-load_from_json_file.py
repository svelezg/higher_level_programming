#!/usr/bin/python3
"""
This is the "8-load_from_json_file" module.
It supplies one function, load_from_json_file.
"""

import json


def load_from_json_file(filename):
    """load_from_json_file"""

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
