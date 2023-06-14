#!/usr/bin/python3
def roman_to_int(s):
    if (s is None) or (type(s) is not str):
        return 0
    roman_characters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = len(roman_characters)
    integer = roman_characters[s[n - 1]]
    for i in range(n - 1, 0, -1):
        c = roman_characters[s[i]]
        p = roman_characters[s[i - 1]]
        integer += p if p >= c else -p
    return integer
