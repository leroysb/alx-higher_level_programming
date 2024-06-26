#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
