#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """geometry class"""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator methode
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
