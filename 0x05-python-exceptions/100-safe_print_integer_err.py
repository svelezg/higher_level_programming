#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        result = True
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        result = False
    return result
