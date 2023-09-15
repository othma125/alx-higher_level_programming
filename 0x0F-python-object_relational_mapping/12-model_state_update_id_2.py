#!/usr/bin/python3
""" Module update the State object with id = 2 to “New Mexico”
        to the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ update the State object with id = 2 to “New Mexico”
        to the database hbtn_0e_6_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state_to_update = session.query(State).filter(State.id == 2).first()
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
        else:
            print("State with id 2 not found.")
