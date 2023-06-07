#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = number % 10
if last_num > 5:
    print("Last digit of {} is {}".format(number, last_num))
elif last_num == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif last_num < 6 and last_num != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_num))
