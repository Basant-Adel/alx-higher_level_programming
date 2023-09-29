#!/usr/bin/python3
""" script that takes your GitHub -> (username and password) """
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    """ Package requests and sys """
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
