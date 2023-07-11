#!/usr/bin/python3
"""to_json_string module"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an object
    :return: string
    :rtype: str
    """
    from json import dumps
    return dumps(my_obj)
