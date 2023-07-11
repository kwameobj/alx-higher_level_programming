#!/usr/bin/python3
"""100-my_int.py - class MyInt that inherits from int"""


class MyInt(int):
    """Creates class MyInt"""

    def __eq__(self, other):
        """inverts =="""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """inverts !="""
        return int.__eq__(self, other)
