#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""
from urllib import request as rq
from urllib import error as er
from sys import argv


if __name__ == "__main__":
    try:
        with rq.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except er.HTTPError as e:
        print("Error code: {}".format(e.code))
