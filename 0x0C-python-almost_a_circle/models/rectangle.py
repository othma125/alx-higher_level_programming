#!/usr/bin/python3
""" class Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, identifier=None):
        """ constructor """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(identifier)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle object """
        return self.__width * self.__height

    def display(self):
        """ displays a rectangle """
        str_format = self.__y * "\n"
        for _ in range(self.__height):
            str_format += (" " * self.__x)
            str_format += ("#" * self.__width) + "\n"
        print(str_format, end='')

    def __str__(self):
        """ str special method """
        str_rectangle = f"[{self.__class__.__name__}] "
        identifier = f"({self.id}) "
        x_y = f"{self.__x}/{self.__y} - "
        w_h = f"{self.__width}/{self.__height}"

        return str_rectangle + identifier + x_y + w_h

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) > 0:
            keys = ['x', 'width', 'id', 'height', 'y']
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns a dictionary with properties """
        return {k: getattr(self, k)
                for k in ['x', 'width', 'id', 'height', 'y']}
