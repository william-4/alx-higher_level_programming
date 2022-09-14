#!/usr/bin/python3
""" A script that lists all State objects containing
the letter a
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]),
                               pool_pre_pint=True)
        Base.metadata.create_all(engine)

        session = Session(engine)
        for state in session.query(State).order_by(State.id).filter(
                State.name.like('%a%')):
            print("{}: {}".format(state.id, state.name))
        session.close()
