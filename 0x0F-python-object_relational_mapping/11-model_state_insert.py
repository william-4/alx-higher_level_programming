#!/usr/bin/python3
"""
A script that adds the State object 'Louisiana' to db
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]),
                               poop_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()
        print(louisiana.id))
        session.close()
