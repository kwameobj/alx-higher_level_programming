#!/usr/bin/python3
"""1-write_file.py - writes a string to a txt file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns
    the number of characters written
    """
    i = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            i += 1
    return count
