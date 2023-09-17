#!/usr/bin/python3
""" This is a Module that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db_connection = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_password,
        database=database_name,
        port=3306
    )

    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = db_cursor.fetchall()
    for state in rows:
        print(state)

    db_connection.close()
