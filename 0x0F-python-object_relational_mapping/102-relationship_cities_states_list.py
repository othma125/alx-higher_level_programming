#!/usr/bin/python3
""" Module that lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == "__main__":
    """ lists all lists all City objects from the database hbtn_0e_101_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        for city in session.query(City).order_by(City.id):
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
