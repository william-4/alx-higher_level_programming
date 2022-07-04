#!/usr/bin/python3
"""
Defines MyList class that inherits from the list class
"""


class MyList(list):
    """a subclass that inherits from the list class"""
    def __init__(self):
        """initialization of an instance"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
