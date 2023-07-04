#!/usr/bin/python3
"""Creates rectangle class"""


class Rectangle:
    """Creates class rectangle class
       with private instance attributes width and height

    Attributes:
        width: width of rectangle
        height: height of rectangle

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Initialises a private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width and raises an error
           if it is not a positive integer
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Initialises a private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height and raises an error
           if it not a positive integer
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the aea of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """alculates the perimeter of the rectangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """print the rectangle with the character #"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
