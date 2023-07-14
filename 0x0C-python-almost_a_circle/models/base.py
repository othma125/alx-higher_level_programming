#!/usr/bin/python3
""" Module that contains class Base """
from json import dumps, loads
from json import dump, loads
# import csv
# import os.path


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, identifier=None):
        """ constructor """
        if identifier is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = identifier

    @classmethod
    def create(cls, **dictionary):
        """ create class method """
        obj = cls(1) if cls.__name__ == 'Base' else cls(1, 1)
        if dictionary is not None and len(dictionary) > 0:
            obj.update(**dictionary)
        return obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        list_dic = []
        if list_objs is not None:
            list_dic = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", mode='w') as file:
            file.write(f'{cls.to_json_string(list_dic)}')

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if not json_string:
            return []
        return loads(json_string)
