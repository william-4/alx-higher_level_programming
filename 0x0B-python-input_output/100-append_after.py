#!/usr/bin/python3
"""
Defines a function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a specific string in a file

    Args:
        filename: name of the file.
        search_string: string to search for
        new_string: string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
