#!/usr/bin/python3
"""module of a function that prints a square with the character #
"""


def print_square(n):
    """
    a function that prints a square with the character #
    :param n:
    :type : integer
    :return: none
    :rtype: none
    """
    if type(n) is not int:
        raise TypeError('size must be an integer')
    if n < 0:
        raise ValueError('size must be >= 0')
    if n == 0:
        print()
    for _ in range(n):
        print('#' * n)
