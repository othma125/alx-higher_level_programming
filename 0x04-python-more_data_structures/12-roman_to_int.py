#!/usr/bin/python3
def roman_to_int(s):
    if (s is None) or (type(s) is not str):
        return 0
    ro_char = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    new_value = 0
    old_value = 0
    for x in s:
        new_value = ro_char[x]
        if new_value <= (old_value if old_value > 0 else 1000000):
            integer += new_value
        else:
            integer -= 2 * old_value
            integer += new_value
        old_value = new_value
    return integer
