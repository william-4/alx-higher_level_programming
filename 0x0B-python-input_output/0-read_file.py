#!/usr/bin/python3
"""
Defines a function that reads a text file without importing any module
"""


def read_file(filename=""):
    """
    The function takes in a file, reads it and prints to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
