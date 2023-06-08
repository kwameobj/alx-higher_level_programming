#!/usr/bin/python3
for i in range(122, 96, 64):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
        continue
    print("{}".format(chr(i - 32)), end="")
