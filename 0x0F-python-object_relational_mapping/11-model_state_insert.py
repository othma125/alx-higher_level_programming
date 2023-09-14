#!/usr/bin/python3
""" Module that add the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ add the State object “Louisiana” to the database hbtn_0e_6_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        print(new_state.id)
