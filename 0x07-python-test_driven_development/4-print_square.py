#!/usr/bin/python3
"""
A module that defines a function which prints a square

It only defines one function
"""
def print_square(size):
    """
    Prints a square using '#'
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
