#!/usr/bin/python3
"""
Function read_file
"""


def save_to_json_file(my_obj, filename):
    """
    reads a file and prints it
    """
    import json
    with open(filename, "a") as f:
        f.write(json.dumps(my_obj))
