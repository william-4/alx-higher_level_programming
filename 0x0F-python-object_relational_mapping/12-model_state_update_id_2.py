#!/usr/bin/python3
""" A script that adds the State object 'Louisiana' to our db
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    request = session.query(State).filter(State.id == 2).first()
    request.name = "New Mexico"
    session.commit()
    session.close()
