#!/usr/bin/python3
"""
This is the 0-add_integer module
It contains one function, add_integer(a, b)
"""


def add_integer(a, b=98):
    """Returns a + b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b,  (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
