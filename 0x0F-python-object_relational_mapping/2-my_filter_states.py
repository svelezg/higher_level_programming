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
    my_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=my_user,
                         passwd=my_pass,
                         db=my_db)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE BINARY '{:s}'
    ORDER BY states.id ASC""".format(my_state))

    rows = cur.fetchall()
    for row in rows:
        print(row)
