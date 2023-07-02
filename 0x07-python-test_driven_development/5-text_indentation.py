#!/usr/bin/python3
"""text-indentation module"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'
    :param text:
    :type text: str
    :return: none
    :rtype: none
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1
    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".:?":
                print()
                print()
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
