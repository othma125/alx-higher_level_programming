#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password) and
uses the Github API to display your id."""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    basic_auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=basic_auth)
    print(r.json().get('id'))
