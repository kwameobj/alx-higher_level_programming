#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """
    Base class

    Attributes:
        __nb_objects: number of objects
        id: id of object

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing method

        args:
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#    def int_val(self, name, value):
#        """checks if value is integer"""
#        if type(value) is not int:
#            raise TypeError("{} must be an integer".format(name))
#        if value <= 0:
#            raise ValueError("{} must be >= 0".format(name))

#    def int_val2(self, name, value):
#        """checks if value is integer"""
#        if type(value) is not int:
#            raise TypeError("{} must be an integer".format(name))
#        if value <= 0:
#            raise ValueError("{} must be >= 0".format(name))
