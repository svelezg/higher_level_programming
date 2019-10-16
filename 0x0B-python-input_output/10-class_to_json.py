#!/usr/bin/python3
"""
This is the "10-class_to_json" module.
It supplies one class, class_to_json.
"""

import json

def class_to_json(obj):
    """class_to_json function"""

    if obj.__dict__:
        return obj.__dict__
