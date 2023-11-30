#!/usr/bin/python3
"""
This is the module 4-print_square.
It contains one function: print_square
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
        return
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
