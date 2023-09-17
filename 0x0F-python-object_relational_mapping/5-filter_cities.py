#!/usr/bin/python3
""" Ia a Module that lists cities of a state by name arg """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    mysql_username, mysql_password, database_name, state_name = argv[1:5]

    db_config = {
        "host": 'localhost',
        "user": mysql_username,
        "passwd": mysql_password,
        "database": database_name,
        "port": 3306
    }

    query = """SELECT cities.name FROM cities
    LEFT JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC"""

    with MySQLdb.connect(**db_config) as db:
        with db.cursor() as cursor:
            cursor.execute(query, (state_name,))
            rows = cursor.fetchall()

    cities = [city[0] for city in rows]
    cities_concat = ", ".join(cities)
    print(cities_concat)
