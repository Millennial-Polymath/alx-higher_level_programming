#!/usr/bin/python3
"""
Prints the state object with the name passed as argument from the database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3360/{}".
                           format(argv[1], argv[2], argv[3]), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    state_arg = argv[4]
    flag = 0
    for state in query:
        if state.name == state_arg:
            print("{}".format(state.id))
            flag = 1
            break

    if flag == 0:
        print("Not found")
