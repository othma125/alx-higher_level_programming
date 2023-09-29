#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv


if __name__ == "__main__":
    q = argv[1] if len(argv) == 2 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_dict = r.json()
        if r_dict == {}:
            print("No result")
        else:
            print(f"[{r_dict.get('id')}] {r_dict.get('name')}")
    except ValueError:
        print("Not a valid JSON")
