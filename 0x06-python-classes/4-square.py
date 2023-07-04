#!/usr/bin/python3
"""Creates a class square"""


class Square:
    """Creates a class called Square"""

    def __init__(self, size=0):
        """Initializes the attritube(s) of the class Square

        Args:
            size(int): The size of the class square
        """
        self.size = size

    @property
    def size(self):
        """Gets a private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of private attribute size and
           raises an error is it is not a positive integer"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size
