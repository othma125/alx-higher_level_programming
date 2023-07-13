#!/usr/bin/python3
""" Module that contains class Base """
from json import dumps, loads
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
