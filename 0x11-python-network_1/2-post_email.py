#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response."""
from urllib import request as rq
from urllib import parse as ps
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = ps.urlencode({'email': email}).encode('utf-8')
    req = rq.Request(url, data)
    with rq.urlopen(req) as response:
        print(response.read().decode('utf-8'))
