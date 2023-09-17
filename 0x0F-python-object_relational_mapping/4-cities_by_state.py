
#!/usr/bin/python3
""" This a Module that lists all cities and their states from database """

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
    db_cursor.execute(
        """SELECT cities.id, cities.name, states.name FROM cities
        JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC"""
    )
    rows = db_cursor.fetchall()
    for city in rows:
        print(city)

    db_cursor.close()
    db_connection.close()
