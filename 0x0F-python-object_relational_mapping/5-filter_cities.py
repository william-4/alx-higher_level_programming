#!/usr/bin/python3
"""
A script that lists all cities from the db hbtn_0e_4_usa
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON \
    cities.state_id=states.id WHERE states.name=%s \
    ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
