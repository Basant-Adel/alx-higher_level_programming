#!/usr/bin/python3
""" script that takes in a URL -> print `ZZ-> Error code """
import sys
import requests

if __name__ == "__main__":
    """ Packages requests and sys """
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
