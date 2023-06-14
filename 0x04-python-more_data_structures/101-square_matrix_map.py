#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        return None
    return list(map(lambda row: list(map(lambda value: value**2, row)), matrix))
