#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    if n == 2:
        t1 = tuple_a
    elif n == 1:
        t1 = (tuple_a[0], 0)
    elif n == 0:
        t1 = (0, 0)
    else:
        t1 = (tuple_a[0], tuple_a[1])
    n = len(tuple_b)
    if n == 2:
        t2 = tuple_b
    elif n == 1:
        t2 = (tuple_b[0], 0)
    elif n == 0:
        t2 = (0, 0)
    else:
        t2 = (tuple_b[0], tuple_b[1])
    return t1[0] + t2[0], t1[1] + t2[1]
