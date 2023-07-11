#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""
def lookup(obj):
    """
    lookup returns the list of available attributes and methods
    

    Args:
        Obj(object): An object to be parsed

    Returns:
        list of available attributes and methods of an object.
    """
    return dir(obj)
