#!/usr/bin/python3
"""Square file"""


class Square:
    """Square class"""

    def __init__(self, n=0, position=(0, 0)):
        """class constructor"""
        if type(n) is not int:
            raise TypeError('size must be an integer')
        if n < 0:
            raise ValueError('size must be >= 0')
        self.__size = n
        if type(position) is not tuple or len(position) != 2 or any(
                type(num) is not int for num in position)\
                or any(num < 0 for num in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, position):
        """position setter"""
        if type(position) is not tuple or len(position) != 2 or any(
                type(num) is not int for num in position)\
                or any(num < 0 for num in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def my_print(self):
        """print square with # and spaces"""
        if self.__size == 0:
            print()
        for _ in range(self.__position[-1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """print square with # and spaces"""
        s = '' if self.__size == 0 else '\n' * self.__position[-1]
        for i in range(self.__size):
            s += ' ' * self.__position[0]
            s += '#' * self.__size
            s += '\n' if i < self.__size - 1 else ''
        return s
