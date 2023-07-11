#!/usr/bin/python3
"""student module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary description with simple data structure"""
        if type(attrs) == list and all(type(att) == str for att in attrs):
            return {att: getattr(self, att) for att in attrs if hasattr(self, att)}
        return self.__dict__
