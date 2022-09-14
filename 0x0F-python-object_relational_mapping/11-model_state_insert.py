#!/usr/bin/python3
"""
A script that adds the State object 'Louisiana' to db
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'\
                               .format(argv[1], argv[2], argv[3]), poop_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)
        session.add(State(name="Louisiana"))
        new = session.query(State).filter(State.name == "Louisiana").first()
        session.commit()
        print("{}".format(new.id))
        session.close()
