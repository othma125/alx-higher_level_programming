#!/usr/bin/python3
"""write_file module"""


def append_write(filename="", text=""):
    """
    write txt to filename with append mode
    :param text:
    :type text:
    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        print(text, file=f, end='')
        return len(text)
