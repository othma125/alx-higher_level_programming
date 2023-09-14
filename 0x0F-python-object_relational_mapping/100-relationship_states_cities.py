#!/usr/bin/python3
""" Module that creates the State “California” with the
    City “San Francisco” from the database hbtn_0e_100_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """ creates the State “California” with the
        City “San Francisco” from the database hbtn_0e_100_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_state = State(name='California')
        new_state.cities = [City(name='San Francisco')]
        session.add(new_state)
        session.commit()
