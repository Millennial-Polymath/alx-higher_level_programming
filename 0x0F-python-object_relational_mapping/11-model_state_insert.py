#!/usr/bin/python3
"""
Adds the state object "Lousiana" to the db
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_obj = State(name="Louisiana")
    session.add(state_obj)
    session.commit()
    print(state_obj.id)
