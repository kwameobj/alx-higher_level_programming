#!/usr/bin/python3
"""2-is_same_class.py"""


def is_same_class(obj, a_class):
    """
    is_same_class is a function that returns True if the object
    is exactly an instance of the specified class

    Args:
        obj: an object
        a_class: a class

    Returns:
        a boolean
    """
    return type(obj) == a_class
