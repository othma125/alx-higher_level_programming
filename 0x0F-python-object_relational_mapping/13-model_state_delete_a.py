#!/usr/bin/python3
""" Module that deletes all State objects with a name containing
        the letter a from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ deletes all State objects with a name containing
        the letter a from the database hbtn_0e_6_usa
    """
    engine = create_engine(f'mysql+mysqldb://{argv[1]}'
                           f':{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.query(State).filter(State.name.like('%a%'))\
            .delete(synchronize_session=False)
        session.commit()
