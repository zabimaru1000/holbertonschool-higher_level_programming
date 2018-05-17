#!/usr/bin/python3
"""
Function read_file
"""


def from_json_string(my_str):
    """
    reads a file and prints it
    """
    import json
    return json.loads(my_str)
