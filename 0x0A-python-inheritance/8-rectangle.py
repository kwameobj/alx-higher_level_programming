#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Creates class Rectangle that inherits BaseGeometry"""
    def __init__(self, width, height):
        """
        Initialises the attributes width and height and
        validates if they are positive integers

        Args:
            width (int): measure of one side of the rectangle
            heing (int): measure of one side of the rectangle

        Return:
            The class
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
