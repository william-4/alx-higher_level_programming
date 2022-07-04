#!/usr/bin/python3
"""
Defines a function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or an instance of a class that
    inherits from the specified class

    Args:
    obj: the object to check
    a_class: the class to check against

    Return:
    True if obj is an instance, otherwise return false
    """
    if isinstance(obj, a_class):
        return True
    return False
