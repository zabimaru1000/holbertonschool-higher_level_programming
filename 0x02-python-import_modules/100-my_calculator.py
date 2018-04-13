#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ac = len(sys.argv)
    av = sys.argv
    op = av[2]
    a = int(av[1])
    b = int(av[3])

    if ac < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif op == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))

    elif op == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))

    elif op == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))

    elif op == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
