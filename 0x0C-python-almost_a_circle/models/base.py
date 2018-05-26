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
        if json_string is None or len(json_string) is 0:
            return empty_list
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns instance with set attributes
        """
        if cls.__name__ is "Rectangle":
            dumbinstance = cls(69, 69)

        elif cls.__name__ is "Square":
            dumbinstance = cls(69)

        dumbinstance.update(**dictionary)
        return dumbinstance

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns list of instances
        """
        empty_list = []
        filename = "{}.json".format(cls.__name__)

        if empty_list is None:
            return empty_list

        with open(filename, "r") as f:
            load = cls.from_json_string(f.read())
        for i in load:
            empty_list.append(cls.create(**i))
        return empty_list
