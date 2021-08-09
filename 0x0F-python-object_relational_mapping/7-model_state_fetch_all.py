#!/usr/bin/python3
"""
Lists all the state objects from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    for state in query:
        print("{}:{}".format(state.id, state.name))
