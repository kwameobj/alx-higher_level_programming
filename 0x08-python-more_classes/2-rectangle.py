#!/usr/bin/python3
"""Defines rectangle class
"""


class Rectangle:
    """Creates class rectangle class
       with private instance attributes width and height

    Attributes:
        width: width of rectangle
        height: height of rectangle

    """

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Initialises a private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width and raises an error
           if it is not a positive integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Initialises a private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height and raises an error
           if it not a positive integer
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the aea of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
