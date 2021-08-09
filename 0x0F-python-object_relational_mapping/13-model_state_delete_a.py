#!/usr/bin/python3
"""
Deletes all state objects with a name containing the letter a from a database
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3360/{}"
                           .format(argv[1], argv[2], argv[3]), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for state in query:
        if "a" in state.name:
            session.delete(state)
    session.commit()
