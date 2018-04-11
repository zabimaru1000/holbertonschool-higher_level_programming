#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        result = number % 10
    elif number < 0:
        result = number % -10

    if result < 0:
        result = result * -1
    print(result, end="")
    return result
