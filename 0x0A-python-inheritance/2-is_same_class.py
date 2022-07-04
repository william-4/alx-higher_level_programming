#!/usr/bin/python3
"""
module defining a function that checks for a class of a function
"""


def is_same_class(obj, a_class):
    """
    Checks if an object obj is exactly an instance of a class a_class.

    Args:
    obj: the object
    a_class: the class to match to

    Returns:
    True if obj is exactly an instance of a_class
    Else returns False

    """
    if type(obj) == a_class:
        return True
    return False
