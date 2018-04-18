#!/usr/bin/python3
def max_integer(my_list=[]):
    #initialize variable to the first element of list
    max = my_list[0]

    #Until i reaches the last element of list, compare two numbers
    for i in range(len(my_list)):
        if max < my_list[i]:
            max = my_list[i]

    return max
