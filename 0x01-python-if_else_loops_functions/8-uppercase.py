#!/usr/bin/python3
def uppercase(s):
    n = ord('A') - ord('a')
    for c in s:
        print(f"{chr(n + ord(c)) if 97 <= ord(c) <= 122 else c}", end="")
    print()
