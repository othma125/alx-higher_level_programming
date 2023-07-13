#!/usr/bin/python3
""" Module for test Square class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base.__nb_objects = 0

    def test_01new_square(self):
        """ Test new square """
        sq = Square(3)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.width, 3)
        self.assertEqual(sq.height, 3)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 1)
        sq = Square(2, 5, 5, 4)
        self.assertEqual(sq.size, 2)
        self.assertEqual(sq.width, 2)
        self.assertEqual(sq.height, 2)
        self.assertEqual(sq.x, 5)
        self.assertEqual(sq.y, 5)
        self.assertEqual(sq.id, 4)

    def test_01new_squares(self):
        """ Test new squares """
        sq = Square(1, 1)
        self.assertFalse(sq is Square(1, 1))
        self.assertFalse(sq.id == Square(1, 1).id)

    def test_02is_Base_instance(self):
        """ Test Square is a Base instance """
        self.assertTrue(isinstance(Square(1), Base))

    def test_03is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """
        self.assertTrue(isinstance(Square(1), Rectangle))

    def test_04incorrect_amount_attrs(self):
        """ Test error raise with no args passed """
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1)

    def test_05access_private_attrs(self):
        """ Trying to access to a private attribute """
        sq = Square(1)
        with self.assertRaises(AttributeError):
            sq.__width
        sq = Square(1)
        with self.assertRaises(AttributeError):
            sq.__height
        sq = Square(1)
        with self.assertRaises(AttributeError):
            sq.__x
        sq = Square(1)
        with self.assertRaises(AttributeError):
            sq.__y

    def test_06valid_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            Square("2", 2, 2, 2)
        with self.assertRaises(TypeError):
            Square(2, "2", 2, 2)
        with self.assertRaises(TypeError):
            Square(2, 2, "2", 2)

    def test_07value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -1)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_08area(self):
        """ Checking the return value of area method """
        sq = Square(4)
        self.assertEqual(sq.area(), 16)
        sq = Square(2)
        self.assertEqual(sq.area(), 4)
        sq.size = 5
        self.assertEqual(sq.area(), 25)

    def test_09display(self):
        """ Test string printed """
        sq = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), res)
        sq = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), res)
        sq.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), res)
        sq = Square(4, 2, 2)
        res = "[Square] (15) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), res)
        sq = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), res)
        sq.id = 1
        sq.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), res)
        sq = Square(5, 2, 1)
        res = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), res)
        sq = Square(3)
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), res)
        sq.x = 1
        res = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), res)
        sq.y = 2
        res = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), res)

    def test_10str(self):
        """ Test __str__ return value """
        sq = Square(5)
        res = "[Square] (18) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), res)
        s2 = Square(3, 7, 1)
        res = "[Square] (19) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(s2)
            self.assertEqual(out.getvalue(), res)
        sq = Square(1, 1, 1)
        res = "[Square] (20) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), res)
        sq = Square(3)
        res = "[Square] (21) 0/0 - 3"
        self.assertEqual(str(sq), res)

    def test_11update(self):
        """ Test update method """
        sq = Square(3)
        res = "[Square] (22) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq = Square(3)
        res = "[Square] (23) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq = Square(1)
        res = "[Square] (24) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq.update(y=3)
        res = "[Square] (2) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq.update(id=1, size=10)
        res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq = Square(10)
        res = "[Square] (25) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        dic = {'size': 3, 'y': 5}
        sq.update(**dic)
        res = "[Square] (25) 0/5 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        sq = Square(7)
        res = "[Square] (26) 0/0 - 7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), res)
        dic = {'id': 10, 'x': '5', 'y': 5}
        with self.assertRaises(TypeError):
            sq.update(**dic)

    def test_12to_dictionary(self):
        """ Test dictionary returned """
        sq = Square(1, 2, 3)
        res = "[Square] (27) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), res)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.width, 1)
        self.assertEqual(sq.height, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 27)
        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(type(sq.to_dictionary()))
            self.assertEqual(out.getvalue(), res)

    # def test_to_dictionary_2(self):
    #     """ Test dictionary returned """
    #     s1 = Square(2, 2, 2)
    #     res = "[Square] (1) 2/2 - 2\n"
    #     with patch('sys.stdout', new=StringIO()) as str_out:
    #         print(s1)
    #         self.assertEqual(str_out.getvalue(), res)
    #
    #     s2 = Square(5)
    #     res = "[Square] (2) 0/0 - 5\n"
    #     with patch('sys.stdout', new=StringIO()) as str_out:
    #         print(s2)
    #         self.assertEqual(str_out.getvalue(), res)
    #
    #     s1_dictionary = s1.to_dictionary()
    #     s2.update(**s1_dictionary)
    #
    #     self.assertEqual(s1.width, s2.width)
    #     self.assertEqual(s1.height, s2.height)
    #     self.assertEqual(s1.x, s2.x)
    #     self.assertEqual(s1.y, s2.y)
    #     self.assertEqual(s1.id, s2.id)
    #
    #     res = "<class 'dict'>\n"
    #     with patch('sys.stdout', new=StringIO()) as str_out:
    #         print(type(s1_dictionary))
    #         self.assertEqual(str_out.getvalue(), res)
    #
    # def test_dict_to_json(self):
    #     """ Test Dictionary to JSON string """
    #     s1 = Square(2)
    #     dictionary = s1.to_dictionary()
    #     json_dictionary = Base.to_json_string([dictionary])
    #     res = "[{}]\n".format(dictionary.__str__())
    #
    #     with patch('sys.stdout', new=StringIO()) as str_out:
    #         print(json_dictionary)
    #         self.assertEqual(str_out.getvalue(), res.replace("'", "\""))
    #
    # def test_json_file(self):
    #     """ Test Dictionary to JSON string """
    #     s1 = Square(2)
    #     dictionary = s1.to_dictionary()
    #     json_dictionary = Base.to_json_string([dictionary])
    #     res = "[{}]\n".format(dictionary.__str__())
    #     res = res.replace("'", "\"")
    #
    #     with patch('sys.stdout', new=StringIO()) as str_out:
    #         print(json_dictionary)
    #         self.assertEqual(str_out.getvalue(), res)
    #
    #     Square.save_to_file([s1])
    #     res = "[{}]".format(dictionary.__str__())
    #     res = res.replace("'", "\"")
    #
    #     with open("Square.json", "r") as file:
    #         res2 = file.read()
    #
    #     self.assertEqual(res, res2)
    #
    # def test_value_square(self):
    #     """ Test value pased to Square """
    #     with self.assertRaises(ValueError):
    #         s1 = Square(-1)
    #
    # def test_create(self):
    #     """ Test create method """
    #     dictionary = {'id': 89}
    #     s1 = Square.create(**dictionary)
    #     self.assertEqual(s1.id, 89)
    #
    # def test_create_2(self):
    #     """ Test create method """
    #     dictionary = {'id': 89, 'size': 1}
    #     s1 = Rectangle.create(**dictionary)
    #     self.assertEqual(s1.id, 89)
    #     self.assertEqual(s1.size, 1)
    #
    # def test_create_3(self):
    #     """ Test create method """
    #     dictionary = {'id': 89, 'size': 1, 'x': 2}
    #     s1 = Rectangle.create(**dictionary)
    #     self.assertEqual(s1.id, 89)
    #     self.assertEqual(s1.size, 1)
    #     self.assertEqual(s1.x, 2)
    #
    # def test_create_4(self):
    #     """ Test create method """
    #     dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
    #     s1 = Rectangle.create(**dictionary)
    #     self.assertEqual(s1.id, 89)
    #     self.assertEqual(s1.size, 1)
    #     self.assertEqual(s1.x, 2)
    #     self.assertEqual(s1.y, 3)
    #
    # def test_load_from_file(self):
    #     """ Test load JSON file """
    #     load_file = Square.load_from_file()
    #     self.assertEqual(load_file, load_file)
    #
    # def test_load_from_file_2(self):
    #     """ Test load JSON file """
    #     s1 = Square(5)
    #     s2 = Square(8, 2, 5)
    #
    #     linput = [s1, s2]
    #     Square.save_to_file(linput)
    #     loutput = Square.load_from_file()
    #
    #     for i in range(len(linput)):
    #         self.assertEqual(linput[i].__str__(), loutput[i].__str__())
