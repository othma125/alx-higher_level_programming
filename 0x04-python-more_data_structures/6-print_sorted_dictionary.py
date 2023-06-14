#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    n = len(a_dictionary)
    i = 0
    for key in sorted(a_dictionary.keys()):
        line_end = '\n' if i + 1 < n else ''
        print('{}: {}'.format(key, a_dictionary[key]), end=line_end)
        i += 1
