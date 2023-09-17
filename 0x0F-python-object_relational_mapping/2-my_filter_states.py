#!/usr/bin/python3
""" Write a script to take in argument and displays all values in states table """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Results must be sorted in ascending order by states.id """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
