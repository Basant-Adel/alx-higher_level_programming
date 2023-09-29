#!/usr/bin/python3
""" script -> (2) arg in order """
import sys
import requests

if __name__ == "__main__":
    """ Packages requests and sys """
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)

    commits = r.json()
    try:
        for b in range(10):
            print("{}: {}".format(
                commits[b].get("sha"),
                commits[b].get("commit").get("author").get("name")))
    except IndexError:
        pass
