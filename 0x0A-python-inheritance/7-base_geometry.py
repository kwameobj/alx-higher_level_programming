#!/usr/bin/python3
"""creates class BaseGeometry"""


class BaseGeometry:
    """creates class BaseGeometry"""

    def area(self):
        """raises an Exception with a message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value as a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
