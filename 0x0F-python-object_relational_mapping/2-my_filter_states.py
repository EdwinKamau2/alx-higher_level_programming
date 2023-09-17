#!/usr/bin/python3
""" Is a Module that accepts an argument and displays all matching values """

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db_connection = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_password,
        database=database_name,
        port=3306
    )

    db_cursor = db_connection.cursor()
    db_cursor.execute(
        """SELECT * FROM states WHERE name LIKE BINARY '{}'
        ORDER BY id ASC""".format(state_name_searched))
    rows = db_cursor.fetchall()
    for state in rows:
        print(state)

    db_cursor.close()
    db_connection.close()
