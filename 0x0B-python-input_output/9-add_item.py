#!/usr/bin/python3
"""
This is the "9-add_item" module.
It supplies one function, load_from_json_file.
"""


if __name__ == "__main__":
    import sys
    import json
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

    filename = "add_item.json"

    try:
        input_list = load_from_json_file(filename)
    except:
        input_list = []

    for i in range(len(sys.argv))[1:]:
        input_list.append(sys.argv[i])

    save_to_json_file(input_list, filename)
