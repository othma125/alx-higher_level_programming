#!/usr/bin/python3
""""Python script that fetches https://intranet.hbtn.io/status"""
from urllib import request as rq


if __name__ == "__main__":
    with rq.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
