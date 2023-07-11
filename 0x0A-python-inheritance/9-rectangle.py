#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Creates class Rectangle that inherits BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialises the attributes width and height and
        validates if they are positive integers
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the are of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
