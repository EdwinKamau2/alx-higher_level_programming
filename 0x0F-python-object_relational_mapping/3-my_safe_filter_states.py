#!/usr/bin/python3
""" Is a Module that accepts arg, displays matching values, protects from SQLi """

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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    db_cursor.execute(query, (state_name_searched,))
    rows = db_cursor.fetchall()
    for state in rows:
        print(state)

    db_cursor.close()
    db_connection.close()
