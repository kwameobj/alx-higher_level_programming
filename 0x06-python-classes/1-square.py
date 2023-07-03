#!/usr/bin/python3
"""A file that contians python code to create a class
   and name it Square
   """


class Square:
    """Creates a class Square.

    Attributes:
        size (int): the length of one side of the square
    """

    def __init__(self, size):
        """Initializes the attritubes of the class

           Args:
                size(int): The size of the class square
        """
        self.__size = size
