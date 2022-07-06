#!/usr/bin/python3
"""
Defines a function write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
    filename: name of file
    text: the string

    Return:
    number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
