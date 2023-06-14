#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    black_list = []
    for x in my_list:
        if x in black_list:
            continue
        result += x
        black_list.append(x)
    return result
