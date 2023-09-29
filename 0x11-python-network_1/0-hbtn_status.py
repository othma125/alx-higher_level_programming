#!/usr/bin/python3
""""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
