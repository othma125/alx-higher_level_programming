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
    s = []
    while index < len(text):
        s.append(text[index])
        if text[index] in ".?:\n":
            if text[index] in ".:?":
                s.append('\n')
                s.append('\n')
            elif text[index] == '\n':
                i = -2
                try:
                    while s[i] == ' ':
                        del s[i]
                        i -= 1
                except IndexError:
                    pass
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
    for c in s:
        print(c, end='')
