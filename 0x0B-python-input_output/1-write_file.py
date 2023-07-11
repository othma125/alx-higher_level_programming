#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """
    write txt to file name
    :param text:
    :type text:
    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    with open(filename, 'w', encoding="utf-8") as f:
        print(text, file=f, end='')
        return len(text)
