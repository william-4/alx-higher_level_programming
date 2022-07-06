#!/usr/bin/python3
"""
Defines a function from_json_string
"""
import json


def from_json_string(my_string):
    """
    Returns an object(Python data structer) represented by a JSON string
    """
    return json.loads(my_string)
