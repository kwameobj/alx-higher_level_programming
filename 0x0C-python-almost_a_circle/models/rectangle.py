#!/usr/bin/python3
"""defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization method

        args:
            width: width of rectangle
            height: width of rectangle
            x: init variable
            y: init variable
        """
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        return self.__width = value

    @property
    def height(self):
        """private instance attribute height"""
        return self.__height

    @height.setter
    def width(self, value):
        """setter for private instance attribute height"""
        return self.__height = value

    @property
    def x(self):
        """private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for private instance attribute x"""
        return self.__x = value

    @property
    def y(self):
        """private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for private instance attribute y"""
        return self.__y = value
