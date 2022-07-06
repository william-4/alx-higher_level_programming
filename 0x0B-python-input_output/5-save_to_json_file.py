#!/usr/bin/python3
"""
Defines a function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Converts an object to a JSON and writes it to a file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
