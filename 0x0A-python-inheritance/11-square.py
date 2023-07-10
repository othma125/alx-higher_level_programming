#!/usr/bin/python3
"""Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size):
        """ constructor"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """area methode"""
        return self.__size ** 2

    def __str__(self):
        """to string method"""
        return f'[{self.__class__.__name__}] {self.__size}/{self.__size}'
