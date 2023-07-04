#!/usr/bin/python3
"""Creates a class square"""


class Square:
    """Creates a class called Square"""

    def __init__(self, size=0):
        """Initializes the attritube(s) of the class Square

        Args:
            size(int): The size of the class square
        """
        self.__size = size

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if(type(value) is not tuple or len(value) is not 2 or
           type(value[0]) is not int or
           type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(value[0] < 0 or value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.size * self.size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if (self.__size == 0):
            print("")
        for i in range(self.__size):
            print("#" * self.size, end="")
            print("")
