#!/usr/bin/python3
def safe_print_list_integers(lst=[], x=0):
    length = 0
    for i in range(x):
        element = lst[i]
        try:
            print("{:d}".format(element), end='')
        except (ValueError, TypeError):
            pass
        else:
            length += 1
    print()
    return length
