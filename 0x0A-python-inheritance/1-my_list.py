#!/bin/usr/python3
"""Creates class MyList"""
class MyList(list):
    """function that prints sorted items"""
    def print_sorted(self):
        """
        print_sorted is a function that prints the list,
        but sorted (ascending sort)

        Args:
            self: puts the instance of the class there

        Returns:
            a sorted list in ascending order
        """
        print(sorted(self))
