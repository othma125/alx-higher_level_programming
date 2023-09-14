#!/usr/bin/python3
""" Module that contains a script that lists all states from the database
    hbtn_0e_0_usa
"""
from MySQLdb import connect
from sys import argv

if __name__ == '__main__':
    """ The code is not executed when imported
    """
    # Open database connection
    with connect(host="localhost", port=3306, user=argv[1],
    passwd=argv[2], db=argv[3]) as db:

        # prepare a cursor object using cursor() method
        with db.cursor() as cursor:
            # execute SQL query using execute() method.
            cursor.execute("SELECT * FROM states ORDER BY id ASC")

            # Fetch a single row using fetchone() method.
            rows = cursor.fetchall()

        # print rows
        for row in rows:
            print(row)
