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
    import calculator_1 as c
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {}".format(a, op, b), end='')
    if op == '+':
        print(" = {}".format(c.add(a, b)))
    elif op == '-':
        print(" = {}".format(c.sub(a, b)))
    elif op == '*':
        print(" = {}".format(c.mul(a, b)))
    else:
        print(" = {}".format(c.div(a, b)))
