!/usr/bin/python3
""" A script to list all states from the database hbtn_0e_0_usa """

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
