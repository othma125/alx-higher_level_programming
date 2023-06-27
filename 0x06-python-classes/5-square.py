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

    def area(self):
        """Area calculation"""
        return self.__size ** 2

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, n):
        """size setter"""
        if type(n) is not int:
            raise TypeError('size must be an integer')
        if n < 0:
            raise ValueError('size must be >= 0')
        self.__size = n

    def my_print(self):
        """print square with #"""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print('#' * self.__size)
