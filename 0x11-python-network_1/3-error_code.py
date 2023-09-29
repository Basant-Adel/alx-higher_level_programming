#!/usr/bin/python3
""" Takes in URL -> Body of response -> (decoded in utf-8) """
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    """ Print -> Error code """
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
