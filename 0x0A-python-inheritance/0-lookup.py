#!/usr/bin/python3
"""
This module defines a function that returns a list of attributes
"""


def lookup(obj):
    """
    Returns a list of an object's available attributes
    """
    return (dir(obj))
