#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    mod = number % 10
if number < 0:
    mod = number % -10

if mod > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, mod))

elif mod == 0:
    print("Last digit of {:d} is 0 and is 0".format(number))

elif mod < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, mod))

print("\n")
