#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        return None
    return [[x**2 for x in row] for row in matrix]
