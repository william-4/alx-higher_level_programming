#!/usr/bin/python3
""" 
A script that prints all City objects our db
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state, city in session.query(State, City).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
