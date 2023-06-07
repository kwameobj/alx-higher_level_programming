#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num >= 0:
    last_num = num % 10
else:
    last_num = (abs(num) % 10) * -1

output = 'Last digit of {} is {} and is'

if last_num > 5:
    print((output + ' greater than 5').format(num, last_num))
elif last_num == 0:
    print((output + ' 0').format(num, last_num))
elif last_num < 6 and last_num != 0:
    print((output + ' less than 6 and not 0').format(num, last_num))
