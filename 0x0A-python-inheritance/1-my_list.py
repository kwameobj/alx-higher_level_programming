#!/usr/bin/python3
"""class MyList derived from parent class list"""


class MyList(list):
    """Represents a MyList"""

    def print_sorted(self):
        """
        prints the list, but sorted

        Args:
            self: puts the instance of the class there

        Returns:
            a sorted list in ascending order
        """
        print(sorted(self))
