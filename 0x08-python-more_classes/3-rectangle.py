#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """makes rectangle object"""
    def __init__(self, width=0, height=0):
        """
        Initialize the class Rectangle

        Args:
            width(int): Rectangle width
            height(int): Rectangle height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets width

        Args:
            value(int): value of width

        Raises:
            TypeError: when value type is not integer
            ValueError: when integer value is < 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets height

        Args:
            value(int): value of height

        Raises:
            TypeError: when value type is not integer
            ValueError: when integer value is < 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area"""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """prints the rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            return ("\n".join("#" * self.width for x in range(self.height)))
