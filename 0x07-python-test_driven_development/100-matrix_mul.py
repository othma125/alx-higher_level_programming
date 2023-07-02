#!/usr/bin/python3
"""Multiplication of two matrix module
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
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(row) is not list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(type(element) not in (int, float)
           for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(type(element) not in (int, float)
           for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    b_inv = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        b_inv.append(new_row)
    result = []
    for row in m_a:
        new_row = []
        for col in b_inv:
            prod = 0
            for i in range(len(b_inv[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        result.append(new_row)
    return result
