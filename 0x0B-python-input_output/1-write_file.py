#!/usr/bin/python3
"""1-write_file.py - writes a string to a txt file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns
    the number of characters written
    """
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
    return count
