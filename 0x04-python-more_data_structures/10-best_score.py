#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    mx = 0
    for key in a_dictionary.keys():
        if mx < a_dictionary[key]:
            mx = a_dictionary[key]
    return mx
