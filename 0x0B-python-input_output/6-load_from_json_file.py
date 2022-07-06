#!/usr/bin/python3
"""
Defines a function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Reads a json file and creates a python object from it
    """
    with open(filename) as f:
        return json.load(f)
