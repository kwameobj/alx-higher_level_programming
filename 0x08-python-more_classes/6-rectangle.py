#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the rectangle with default width and height of 0"""
        self.width = width
        self.height = height
        Rectanlge.number_of_instances += 1

    def __del__(self):
        """prints - 'Bye rectangle...' when a Rectangle instance is deleted"""
        Rectanlge.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of Reactangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns string representation of Rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of Rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
