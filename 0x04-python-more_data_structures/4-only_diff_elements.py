#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_set = set()
    for x in set_1:
        if x in set_2:
            continue
        c_set.add(x)
    for x in set_2:
        if x in set_1:
            continue
        c_set.add(x)
    return c_set
