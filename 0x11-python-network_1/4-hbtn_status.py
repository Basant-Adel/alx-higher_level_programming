#!/usr/bin/python3
""" Script that fetches -> (tabulation before -) """
import requests

if __name__ == "__main__":
    """ The Package Requests """
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
