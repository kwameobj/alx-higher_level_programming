#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """
        a function that returns True if the object is an instance
        of a class that inherited (directly or indirectly) from
        the specified class; otherwise False

        Args:
            obj: an object
            a_class: a class


        Returns:
            None
    """
    return type(obj) != a_class and isinstance(obj, a_class)
