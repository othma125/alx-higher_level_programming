#!/usr/bin/python3
""" Module that contains a script that lists all states from the database
    hbtn_0e_0_usa
"""
from MySQLdb import connect
from sys import argv

if __name__ == '__main__':
    """ The code is not executed when imported
    """
    db = connect(host="localhost", port=3306, user=argv[1],
                 passwd=argv[2], db=argv[3])
    with db.cursor() as cursor:
        querry = "SELECT * FROM states"
        querry += " WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(querry)
        for row in cursor.fetchall():
            print(row)
    db.close()
