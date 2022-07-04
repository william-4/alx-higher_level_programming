#!/usr/bin/python3
"""
Defines a class BaseGeometry together with its member methods and attributes
"""


class BaseGeometry:
    """
    defines the class used for practice
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Takes in an value and validates that it is an integer.

        Args:
        name: name of the parameter
        value: the parameter to validate
        Raises:
        TypeError: if value is not an integer
        ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an ingeger".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
