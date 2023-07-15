#!/usr/bin/python3
""" Module that contains class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Rectangle """

    def __init__(self, size, x=0, y=0, identifier=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, identifier)

    def __str__(self):
        """ str special method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.__id)
        str_xy = "{}/{} - ".format(self.__x, self.__y)
        str_wh = "{}/{}".format(self.__width, self.__height)
        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """ Getter size """
        return self.height

    @size.setter
    def size(self, value):
        """ Setter size """
        self.height = value
        self.width = value

    def __str__(self):
        """ str special method """
        str_square = f"[{self.__class__.__name__}] "
        identifier = f"({self.id}) "
        x_y = f"{self.x}/{self.y} - "
        size = f"{self.size}"
        return str_square + identifier + x_y + size

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) > 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        return {k: self.getatt(k) for k in ('id', 'size', 'x', 'y')}

    def getatt(self, k):
        """ Returns attributes """
        return getattr(self, 'width') if k == 'size' else getattr(self, k)
