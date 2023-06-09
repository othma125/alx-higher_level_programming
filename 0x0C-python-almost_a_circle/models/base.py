#!/usr/bin/python3
""" Module that contains class Base """
from json import dumps, loads
from os import path
import csv
import turtle


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

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = f"{cls.__name__}.json"
        if not path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_str = f.read()
        return [cls.create(**dct) for dct in cls.from_json_string(list_str)]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        if cls.__name__ == "Rectangle":
            keys = ['id', 'width', 'height', 'x', 'y']
        else:
            keys = ['id', 'size', 'x', 'y']
        data = []
        if list_objs is not None:
            for obj in list_objs:
                list_dic = [obj.to_dictionary()[key] for key in keys]
                data.append(list_dic)
        with open(f"{cls.__name__}.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)
        if path.exists(filename) is False:
            return []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']
        data = []
        for csv_elem in csv_list:
            dct = {}
            for element in enumerate(csv_elem):
                dct[list_keys[element[0]]] = int(element[1])
            data.append(dct)
        return [cls.create(**d) for d in data]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares
        """
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()
        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
