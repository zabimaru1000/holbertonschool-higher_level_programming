#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i == "c" or i == "C":
            i = ""

        new_str += i
    return new_str
