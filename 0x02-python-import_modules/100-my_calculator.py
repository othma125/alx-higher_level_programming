#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) != 4:
        print("Usage:./ 100 - my_calculator.py < a > < operator > < b >")
        exit(1)
    op = argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {}".format(a, op, b), end='')
    if op == '+':
        from calculator_1 import add
        print(" = {}".format(add(a, b)))
    elif op == '-':
        from calculator_1 import sub
        print(" = {}".format(sub(a, b)))
    elif op == '*':
        from calculator_1 import mul
        print(" = {}".format(mul(a, b)))
    else:
        from calculator_1 import div
        print(" = {}".format(div(a, b)))
