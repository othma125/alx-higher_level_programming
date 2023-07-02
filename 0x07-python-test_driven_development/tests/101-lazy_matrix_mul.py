#!/usr/bin/python3
"""module of multiplication function using NumPy."""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices using numpy
    """

    return matmul(m_a, m_b)
