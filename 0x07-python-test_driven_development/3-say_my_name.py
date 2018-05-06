#!/usr/bin/python3
"""
Module for say_my_name
Uses one function to combine two strings to print
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a full name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
