#!/usr/bin/python3
""" 
This module defines the class City that inherits from Base
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ Class City """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
