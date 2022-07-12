#!/usr/bin/python3
"""
This module defines a class called Base
"""


class Base:
    """
    The base class for all other classes in this project
    """

    ''' private class attribute for number of objects'''
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance

        Args:
        id (int): id of a new Base instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
