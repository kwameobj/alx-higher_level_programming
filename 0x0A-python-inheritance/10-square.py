#!/usr/bin/python3
"""10-square.py: creates a class square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Creates class Square that inherits another class Rectangle"""

    def __init__(self, size):
        """Initialises the side measuremments of the square"""
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)
