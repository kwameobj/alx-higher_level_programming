#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    length = len(str)

    for i in range(0, length):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new_string += chr(ord(str[i]) - 32)
        else:
            new_string += str[i]

    print("{}".format(new_string))
