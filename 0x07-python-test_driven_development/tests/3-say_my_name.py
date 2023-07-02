#!/usr/bin/python3
"""print first and last name module"""


def say_my_name(first_name="", last_name=""):
    """ prints first and last name
        Arguments:
            @first_name: str
            @second_name: str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
