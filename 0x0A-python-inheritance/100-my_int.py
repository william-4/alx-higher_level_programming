#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Invert int operators == and !=
    """

    def __eq__(self, value):
        """
        Interchange == opeartor with !=
        """
        return self.real != value

    def __ne__(self, value):
        """
        Interchange != operator with ==
        """
        return self.real == value
