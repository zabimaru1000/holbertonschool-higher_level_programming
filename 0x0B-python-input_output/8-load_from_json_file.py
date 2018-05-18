#!/usr/bin/python3
"""
load_from_json_file
"""


def load_from_json_file(filename):
    import json
    with open(filename, "r") as file_name:
        return json.load(file_name)
