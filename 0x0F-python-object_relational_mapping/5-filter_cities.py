#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.name
                    FROM cities JOIN states
                    ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id;""", (argv[4],))

    rows = cur.fetchall()
    for index in range(len(rows)):
        if index != 0:
            print(', ', end='')
        print(rows[index][0], end='')
    print('')

    cur.close()
    db.close()
