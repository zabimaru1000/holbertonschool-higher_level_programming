#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.keys())
    for i in range(len(sort)):
        print("{:s}: {}".format(sort[i], a_dictionary[sort[i]]))
