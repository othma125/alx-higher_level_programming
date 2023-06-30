#!/usr/bin/python3
"""matrix divided implementation
"""


def matrix_divided(matrix, div):
    """Function that divide elements of a matrix by a number
    """
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    msg = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list or matrix == []:
        raise TypeError(msg)
    result = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        new_row = []
        for element in row:
            if type(element) in (int, float):
                new_row.append(round(element / div, 2))
            else:
                raise TypeError(msg)
        result.append(new_row)
    return result
