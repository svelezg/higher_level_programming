#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    a = int(argv[1])
    o = argv[2]
    b = int(argv[3])
    r = 0

    if argv[2] is "+":
        r = add(a, b)
    elif argv[2] is "-":
        r = sub(a, b)
    elif argv[2] is "*":
        r = mul(a, b)
    elif argv[2] is "/" and int(argv[3]) != 0:
        r = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {} {:d} = {:d}".format(a, o, b, r))
