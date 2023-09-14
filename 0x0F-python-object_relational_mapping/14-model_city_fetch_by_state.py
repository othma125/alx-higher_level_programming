#!/usr/bin/python3
""" Module that lists all State and cities objects
    from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """ prints all City objects from the database hbtn_0e_14_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        for state, city in session.query(State, City)\
                                  .filter(State.id == City.state_id)\
                                  .order_by(City.id).all():
            print(f'{state.name}: ({city.id}) {city.name}')
