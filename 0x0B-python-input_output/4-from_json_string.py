#!/usr/bin/python3
"""from_json_string module"""


def from_json_string(my_str):
    """
    returns an object from the JSON representation
    :return: object
    :rtype: object
    """
    from json import loads
    return loads(my_str)
