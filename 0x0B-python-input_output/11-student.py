#!/usr/bin/python3
"""
Defines a class Student
"""


class Student:
    """
    Represent a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student
        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student

        Args:
            attrs: The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of Student

        Args:
            json: The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
