#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
    LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
