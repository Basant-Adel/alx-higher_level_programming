#!/usr/bin/python3
""" write script to take in arg and displays all values in states table """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Results must be sorted in ascending order by states.id """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute({'name': argv[4]})
        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
