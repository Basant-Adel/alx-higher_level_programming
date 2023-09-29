#!/usr/bin/python3
""" Write to take in URL -> You must use packages urllib & sys """
import sys
import urllib.request

if __name__ == "__main__":
    """ The X-Request-Id Variable """
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
