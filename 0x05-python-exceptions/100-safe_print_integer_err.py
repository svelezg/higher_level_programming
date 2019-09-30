#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        result = True
    except ValueError as b:
        sys.stderr.write("Exception: {}\n".format(b))
        result False
    except TypeError as b:
        sys.stderr.write("Exception: {}\n".format(b))
        result False
    return result
