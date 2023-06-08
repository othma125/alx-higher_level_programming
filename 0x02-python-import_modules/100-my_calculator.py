#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    if len(argv) != 4:
        print("Usage:./ 100 - my_calculator.py < a > < operator > < b >")
        exit(1)
    op = argv[2]
    if op == '+' or op == '-' or op == '*' or op == '/':
        import calculator_1 as c

        a = int(argv[1])
        b = int(argv[3])
        if op == '+':
            print("{} + {} = {}".format(a, b, c.add(a, b)))
        elif op == '-':
            print("{} - {} = {}".format(a, b, c.sub(a, b)))
        elif op == '*':
            print("{} * {} = {}".format(a, b, c.mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, c.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
