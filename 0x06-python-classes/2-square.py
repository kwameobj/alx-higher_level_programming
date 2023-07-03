#!/usr/bin/python3
"""A file that contians python code to create a class
   and name it Square
   """


class Square:
    """Creates a class Square.

    Attributes:
        size (int): the length of one side of the square
    """

    def __init__(self, size=0):
        """Initializes the attribute "size" of the class
           and raises an error if the vale is not an integer

        Args:
            size (int): size of the class square which

        """
        
        if(type(size) is not int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >=0")
        self.__size = size
