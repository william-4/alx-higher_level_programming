#!/usr/bin/python3
"""
Python script that takes an argument and returns all states that
math the argv[4]
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s\
    ORDER BY id", (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
