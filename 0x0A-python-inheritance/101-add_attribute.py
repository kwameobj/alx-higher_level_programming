#!/usr/bin/python3
"""101-add_attribute.py - adds a new attribute to an object"""


def add_attribute(obj, name=0, value=0):
    """adds an attribute to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
