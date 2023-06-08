#!/usr/bin/python3
from sys import argv
import calculator_1 as c
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
    print(f"{a} {op} {b}", end='')
    if op == '+':
        print(f" = {c.add(a, b)}")
    elif op == '-':
        print(f" = {c.sub(a, b)}")
    elif op == '*':
        print(f" = {c.mul(a, b)}")
    else:
        print(f" = {c.div(a, b)}")
