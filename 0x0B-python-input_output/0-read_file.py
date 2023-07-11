#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """
    Read filename file and print if in stdout
    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end='')
