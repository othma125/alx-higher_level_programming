#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        return area
        :return:
        :rtype:
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns perimeter
        :return:
        :rtype:
        """
        if self.__height * self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of
            the Rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        representation = ''
        for i in range(self.__height):
            representation += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                representation += '\n'
        return representation

    def __repr__(self):
        """Return the canonical representation of
            the Rectangle in printable way.
        """
        s = 'Rectangle(' + str(self.__width)
        s += ', ' + str(self.__height) + ')'
        return s

    def __del__(self):
        """Print a message at deletion of a Rectangle object."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __ge__(self, other):
        return self.area() >= other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 >= rect_2:
            return rect_1
        return rect_2
