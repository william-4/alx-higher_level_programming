#!/usr/bin/python3
"""
Defines a function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if an obj is an instance of a class that inherited, directly
    or indirectly from the specified class

    Args:
    obj: the object to check
    a_class: the class to check against

    Return:
    True if the object is an instance, otherwise returns false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
