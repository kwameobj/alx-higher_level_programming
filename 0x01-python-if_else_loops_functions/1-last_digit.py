#!/usr/bin/python3

# 1-last_digit.py - a python code that randomly generates a number
# and prints its last number with some information

import random
number = random.randint(-10000, 10000)
str_1 = "Last digit of {} is {} and is "

if number >= 0:
    last_num = number % 10
elif number < 0:
    last_num = (abs(number) % 10) * -1

if last_num > 5:
    print((str_1 + "greater than 5").format(number, last_num))
elif last_num == 0:
    print((str_1 + "0").format(number, last_num))
elif last_num < 6 and last_num != 0:
    print((str_1 + "less than 6 and not 0").format(number, last_num))
