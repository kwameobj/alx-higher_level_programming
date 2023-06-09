#!/usr/bin/python3
"""0-read_file.py: reads a text file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
