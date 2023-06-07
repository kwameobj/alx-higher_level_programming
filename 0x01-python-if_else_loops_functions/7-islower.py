#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if i == ord(c):
            return True
    else:
        return False
