#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul
if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage:./ 100 - my_calculator.py < a > < operator > < b >")
        exit(1)
    op = argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = ".format(a, op, b), end='')
    if op == '+':
        print("{}".format(add(a, b)))
    elif op == '-':
        print("{}".format(sub(a, b)))
    elif op == '*':
        print("{}".format(mul(a, b)))
    else:
        print("{}".format(div(a, b)))
