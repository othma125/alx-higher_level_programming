#!/usr/bin/python3
def no_c(my_string):
    s = ''
    for c in my_string:
        if c in 'cC':
            continue
        s += c
    return s
