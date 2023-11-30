#!/usr/bin/python3
import doctest


def add_integer(a, b=98):
    """
    Returns a + b
    >>> 0-add_integer(1, 3)
    4
    >>> 0-add_intger(0, 1)
    1
    >>> 0-add_integer(-1, 0)
    -1
    >>> 0-add_integer(-1, -2)
    -3
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b,  (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

if __name__ == "__main__":
    doctest.testmod()
