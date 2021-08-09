#!/usr/bin/python3
"""
Prints the first state object from a database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3360/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3],
                                   echo=False))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).first()
    if query is None:
        print('Nothing')
    else:
        print("{}: {}".format(query.id, query.name))
