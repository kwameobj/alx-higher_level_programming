#!/usr/bin/python3
"""7-base_geometry.py: creates class BaseGeometry"""


class BaseGeometry:
    """creates class BaseGeometry"""
    def area(self):
        """
        raises an Exception with the message
        "area() is not implemented"

        Args:
            self: self of class

        Return:
            an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
         that validates value
        Args:
            name (string): name of instance
            value (int): value of instance
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
