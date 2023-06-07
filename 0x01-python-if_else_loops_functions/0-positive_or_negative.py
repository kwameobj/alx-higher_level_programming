#!/usr/bin/python3
import random
num = random.randint(-10, 10)
if num > 0:
    print('{} is positive'.format(num))
elif num < 0:
    print('{} is negative'.format(num))
else:
    print('{} is zero'.format(num))
