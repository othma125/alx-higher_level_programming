#!/usr/bin/python3
""" Module that creates the State “California” with the
    City “San Francisco” from the database hbtn_0e_100_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    """ creates the State “California” with the
        City “San Francisco” from the database hbtn_0e_100_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.add(City(name="San Francisco", state=State(name="California")))
        session.commit()
