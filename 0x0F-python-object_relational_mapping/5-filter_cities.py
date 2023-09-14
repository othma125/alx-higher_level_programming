#!/usr/bin/python3
""" Module that contains a script that lists all cites from the database
    with the name of states that it belongs to
"""
from MySQLdb import connect
from sys import argv

if __name__ == '__main__':
    """ The code is not executed when imported
    """
    db = connect(host="localhost", port=3306, user=argv[1],
                 passwd=argv[2], db=argv[3])
    with db.cursor() as cursor:
        query = "SELECT cities.name"
        query += " FROM cities JOIN states ON cities.state_id = states.id"
        query += "ORDER BY id"
        cursor.execute(query)
        print(', '.join([row for row in cursor.fetchall() if row == argv[4]]))
    db.close()
