#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Read filename file and append_after search_string
    :param new_string:
    :type new_string:
    :param search_string:
    :type search_string:
    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    txt = ''

    with open(filename, mode='r', encoding="utf-8") as f:
        for line in f.readlines():
            txt += line + (new_string if search_string in line else '')
    with open(filename, mode='w', encoding="utf-8") as f:
        print(txt, file=f, end='')
append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")