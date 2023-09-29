#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
and uses the Github API to display your id."""

import requests
from sys import argv

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    r = requests.get(url)
    for commit in r.json()[:10]:
        try:
            print(f"{commit.get('sha')}: "
                  f"{commit.get('commit').get('author').get('name')}")
        except IndexError:
            break
