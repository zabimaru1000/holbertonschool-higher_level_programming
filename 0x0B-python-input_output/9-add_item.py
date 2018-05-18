#!/usr/bin/python3
"""
load_from_json_file
"""

import sys

json_list = []
load_file = __import__("8-load_from_json_file.py").load_from_json_file
save_file = __import__("7-save_to_json_file.py").save_to_json_file.py
av = sys.argv

for i in range(len(av)):
    if i >= 1:
        json_list.append(av[i])
save_file(json_list, "add_item.json")
