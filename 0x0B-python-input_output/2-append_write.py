#!/usr/bin/python3
"""2-append_write.py - appends string to end of a text file"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
        f.seek(0)
        if 0 < nb_lines < count:
            for count in range(nb_lines):
                print(f.readline(), end="")
                count += 1
        else:
            for line in f:
                print(line, end="")
