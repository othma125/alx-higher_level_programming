#!/usr/bin/python3
"""add two integers module
    if the a and b are not integers an exception is thrown
    if a or b are floats only the floor is taken into consideration
    otherwise the sum is returned
"""


def matrix_mul(m_a, m_b):
    """
    Multiplication of two matrix
    :param m_a: matrix
    :type m_a: list of lists
    :param m_b: matrix
    :type m_b: list of lists
    :return: new matrix
    :rtype: list of lists
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if a == float('NaN') or b == float('NaN'):
        raise ValueError('cannot convert float NaN to integer')
    s = int(a) + int(b)
    if s == a or s == b:
        raise OverflowError('cannot convert float infinity to integer')
    return s
