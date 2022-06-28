#!/usr/bin/python3
"""
A module defining a function say_my_name
The function prints the first and last names passed to it

"""
def say_my_name(first_name, last_name=""):
    """
    Prints a string containing the first and last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
