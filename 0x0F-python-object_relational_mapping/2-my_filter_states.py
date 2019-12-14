#!/usr/bin/python3
"""
takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
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

    name = sys.argv[4]
    cur.execute("""SELECT *
    FROM states
    WHERE name = '{}'
    ORDER BY id""".format(name))

    rows = cur.fetchall()
    for row in rows:
        print(row)
