#!/usr/bin/python3
def safe_print_list_integers(l=[], x=0):
    length = 0
    for i in range(x):
        element = l[i]
        try:
            print("{:d}".format(element), end='')
        except (ValueError, TypeError):
            pass
        else:
            length += 1
    print()
    return length
