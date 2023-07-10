#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """inherits_from function"""

    return issubclass(obj, a_class) and type(obj) != a_class
