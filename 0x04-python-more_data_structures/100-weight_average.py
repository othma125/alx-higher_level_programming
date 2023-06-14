#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    return sum(map(lambda x: x[0] * x[1], my_list)) / sum(map(lambda x: x[1], my_list))
