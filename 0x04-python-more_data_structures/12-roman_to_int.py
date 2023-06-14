#!/usr/bin/python3
def roman_to_int(s):
    if (s is None) or (type(s) is not str):
        return 0
    ro_char = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    new_value = 0
    for x in s:
        if new_value == 0:
            new_value = ro_char[x]
        elif new_value >= ro_char[x]:
            integer += ro_char[x]
            continue
        else:
            integer -= new_value
            new_value = ro_char[x]
            continue
        integer += new_value
    return integer
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))