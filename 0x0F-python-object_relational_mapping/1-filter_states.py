#!/usr/bin/python3
""" Module that contains a script that lists all states that start with N from
"""
from MySQLdb import connect
from sys import argv

if __name__ == '__main__':
    """ The code is not executed when imported
    """
    db = connect(host="localhost", port=3306, user=argv[1],
                 passwd=argv[2], db=argv[3])
    with db.cursor() as cursor:
        query = "SELECT * FROM states"
        query += " WHERE name LIKE BINARY 'N%' ORDER BY id"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    db.close()
