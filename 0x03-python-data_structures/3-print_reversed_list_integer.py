#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    start = my_list[-1]
    end = my_list[0] - 1
    for i in range(start, end, -1):
        print("{:d}".format(i))
