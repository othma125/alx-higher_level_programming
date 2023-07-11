#!/usr/bin/python3
"""load_from_json_file module"""


def load_from_json_file(filename):
    """
    return an object from the JSON representation written in file
    :return: string
    :rtype: str
    """
    with open(file=filename, mode='r') as file:
        my_str = file.readline()
    from json import loads
    return loads(my_str)
