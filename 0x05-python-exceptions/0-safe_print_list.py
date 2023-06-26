#!/usr/bin/python3
def safe_print_list(l=[], x=0):
    length = 0
    for element in l:
        if length < x:
            try:
                print("{}".format(element), end='')
            except IndexError:
                print()
                break
            else:
                length += 1
    else:
        print()
    return length
