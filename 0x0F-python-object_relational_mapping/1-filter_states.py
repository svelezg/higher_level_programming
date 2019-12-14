#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_db = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=my_user,
                         passwd=my_pass,
                         db=my_db)
    cur = db.cursor()

    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY 'N%' "
                "ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
