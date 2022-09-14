#!/usr/bin/python3
"""
A python script that contains a class definition of State and an
instance Base = declarative_base():
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State to represent our states"""

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
