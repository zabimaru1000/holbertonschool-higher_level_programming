#!/usr/bin/python3
"""
Class Base
"""

import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor init
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method returning a JSON string of dict
        """
        if list_dictionaries is None or list_dictionaries is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method, returns JSON string of argument
        """
        empty_list = []
        if json_string is not None:
            empty_list.append(json_string)
            return empty_list
        else:
            return empty_list

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method writes JSON string to file
        """
        empty_list = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is not None:
            for i in list_objs:
                empty_list.append(cls.to_dictionary(i))
        with open(filename, "w") as f:
            f.write(cls.to_json_string(empty_list))
