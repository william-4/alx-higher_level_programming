#!/usr/bin/python3
"""
A script that prints State table records with the name passed as 
an argument to the script
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'\
                           .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    request = session.query(State).filter(State.name == argv[4]).scalar()
    if request:
        print("{}".format(request.id))
    else:
        print("Not found")
    session.close()
