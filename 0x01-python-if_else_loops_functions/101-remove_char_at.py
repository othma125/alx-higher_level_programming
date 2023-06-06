#!/usr/bin/python3
def remove_char_at(s, n):
    ss = ''
    for i in range(len(s)):
        if i == n:
            continue
        ss += s[i]
    return ss
