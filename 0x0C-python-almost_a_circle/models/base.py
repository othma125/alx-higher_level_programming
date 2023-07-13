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
