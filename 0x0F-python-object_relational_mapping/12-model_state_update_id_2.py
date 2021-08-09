#!/usr/bin/python3
"""
Changes the name of a state object from the database
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
    row = session.query(State).filter(State.id == 2).first()
    row.name = "New Mexico"
    session.commit()
