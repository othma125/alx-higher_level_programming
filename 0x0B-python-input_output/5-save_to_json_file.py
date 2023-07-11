#!/usr/bin/python3
"""save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """
    write the JSON representation of an object in a file
    :return: string
    :rtype: str
    """
    with open(file=filename, mode='w') as file:
        from json import dumps
        print(dumps(my_obj), file=file, end='')
