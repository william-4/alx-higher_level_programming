#!/usr/bin/python3
"""
Defines a function append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
    filename: the name of the file
    text: the string to append

    Return:
    the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
