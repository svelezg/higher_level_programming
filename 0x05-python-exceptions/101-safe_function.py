#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as b:
        sys.stderr.write("Exception: {}\n".format(b))
    return None
