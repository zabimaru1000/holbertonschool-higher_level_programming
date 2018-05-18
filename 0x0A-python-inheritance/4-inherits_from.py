#!/usr/bin/python3
"""
Function is_same_class
"""


def inherits_from(obj, a_class):
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
