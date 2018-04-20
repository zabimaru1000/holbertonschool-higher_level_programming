#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = list(a_dictionary.keys())
    new = {}

    for i in a_dictionary:
        b = a_dictionary[i] * 2
    for j in range(len(a)):
        new = update_dictionary(a_dictionary, a[j], b)
    return new

def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    return a_dictionary
