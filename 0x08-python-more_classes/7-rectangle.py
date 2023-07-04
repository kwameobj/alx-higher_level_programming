#!/usr/bin/python3
""" Defines rectangle class """


class Rectangle:
    """ Rectangle with private instance attributes width and height """

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
        """ Finds the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Validates width as a positive integer """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Finds the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Validates height as a positive integer """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Returns area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns string version of the rectangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """ Returns string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Prints message when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
