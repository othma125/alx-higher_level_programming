#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    if n == 0:
        print()
        return
    for line in matrix:
        for i, x in enumerate(line):
            print("{:d} ".format(x), end='' if i + 1 < n else '\n')
