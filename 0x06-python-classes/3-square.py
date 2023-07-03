#!/usr/bin/python3
class Square:
    """Creates a class called Square.

    """

    def __init__(self, size = 0):
        """Initializes the attritube "size" of the class.

        Args:
            size(int): The size of the class square

        """
        
        if(type(size) is not int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Returns the area of the square.

        """
 
        return(self.__size * self.__size)
