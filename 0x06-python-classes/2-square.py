#!/usr/bin/python3
"""Square file"""


class Square:
    """Square class"""

    def __init__(self, n=0):
        """class constructor"""
        if type(n) is not int:
            raise TypeError('size must be an integer')
        if n < 0:
            raise ValueError('size must be >= 0')
        self.__size = n
