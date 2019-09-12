#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} {}".format(len(sys.argv) - 1, "arguments."))
    else:
        if len(sys.argv) == 2:
            print("{:d} {}".format(len(sys.argv) - 1, "argument:"))
            print("{}: {}".format(1, sys.argv[1]))
        else:
            print("{:d} {}".format(len(sys.argv) - 1, "arguments:"))
            for i in range(len(sys.argv))[1:]:
                print("{:d}: {}".format(i, sys.argv[i]))
