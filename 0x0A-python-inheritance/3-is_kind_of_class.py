#!/usr/bin/python3
"""3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """ a function that returns True if the object is
        an instance of, or if the object is an instance
        of a class that inherited from, the specified class;
        otherwise False

        Args:
            obj: an object
            a_class: a class

        Returns:
            a boolean
    """
    return isinstance(obj, a_class)
