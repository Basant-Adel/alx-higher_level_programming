#!/usr/bin/python3
""" script that takes in a URL -> You must use packages urllib & sys """
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    """ The Email Variable """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
