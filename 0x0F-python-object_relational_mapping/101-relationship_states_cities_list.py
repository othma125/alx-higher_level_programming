#!/usr/bin/python3
""" Module that lists all State objects,
    and corresponding City objects, contained in the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base

if __name__ == "__main__":
    """ lists all State objects,
        and corresponding City objects,
        contained in the database hbtn_0e_101_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        for state in session.query(State).order_by(State.id).all():
            print(f'{state.id}: {state.name}')
            for city in state.cities:
                print(f'\t{city.id}: {city.name}')
