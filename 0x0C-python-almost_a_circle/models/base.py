#!/usr/bin/python3
"""
    Is the base module
"""


import json
from os.path import exists


class Base:
    """ Is the Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This Initializes an instance of Base class """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This Returns JSON representation of dictionary list """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This Writes JSON string representation to a file """
        filename = f"{cls.__name__}.json"
        output_list = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                output_list.append(obj.to_dictionary())
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(output_list))

    @staticmethod
    def from_json_string(json_string):
        """ This Returns Python Object from JSON representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ This Returns a list of instances """
        filename = f"{cls.__name__}.json"
        if exists(filename):
            with open(filename, 'r', encoding="utf-8") as file:
                instances = cls.from_json_string(file.read())
                return [cls.create(**instance) for instance in instances]
        return []
