#!/usr/bin/python3
""" Module for test Square class """
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(TestCase):
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
        self.assertIsNot(sq, Square(1, 1))
        self.assertFalse(sq.id == Square(1, 1).id)

    def test_02is_Base_instance(self):
        """ Test Square is a Base instance """
        self.assertIsInstance(Square(1), Base)

    def test_03is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """
        self.assertIsInstance(Square(1), Rectangle)

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
        output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), output)
        sq = Square(4)
        output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), output)
        sq.size = 5
        output = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), output)
        sq = Square(4, 2, 2)
        output = "[Square] (15) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq = Square(3, 2, 5, 3)
        output = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq.id = 1
        sq.size = 11
        output = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq = Square(5, 2, 1)
        output = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), output)
        sq = Square(3)
        output = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), output)
        sq.x = 1
        output = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), output)
        sq.y = 2
        output = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            sq.display()
            self.assertEqual(out.getvalue(), output)

    def test_10str(self):
        """ Test __str__ return value """
        sq = Square(5)
        output = "[Square] (18) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        s2 = Square(3, 7, 1)
        output = "[Square] (19) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(s2)
            self.assertEqual(out.getvalue(), output)
        sq = Square(1, 1, 1)
        output = "[Square] (20) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq = Square(3)
        output = "[Square] (21) 0/0 - 3"
        self.assertEqual(str(sq), output)

    def test_11update(self):
        """ Test update method """
        sq = Square(3)
        output = "[Square] (22) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq.update(5)
        output = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq = Square(3)
        output = "[Square] (23) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq.update(5)
        output = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq = Square(1)
        output = "[Square] (24) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq.update(2, 2, 2, 2)
        output = "[Square] (2) 2/2 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq.update(y=3)
        output = "[Square] (2) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq.update(id=1, size=10)
        output = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq = Square(10)
        output = "[Square] (25) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        dic = {'size': 3, 'y': 5}
        sq.update(**dic)
        output = "[Square] (25) 0/5 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq = Square(7)
        output = "[Square] (26) 0/0 - 7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        dic = {'id': 10, 'x': '5', 'y': 5}
        with self.assertRaises(TypeError):
            sq.update(**dic)

    def test_12to_dictionary(self):
        """ Test dictionary returned """
        sq = Square(1, 2, 3)
        output = "[Square] (27) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.width, 1)
        self.assertEqual(sq.height, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 27)
        output = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(type(sq.to_dictionary()))
            self.assertEqual(out.getvalue(), output)

    def test_13to_dictionary_2(self):
        """ Test dictionary returned """
        sq = Square(2, 2, 2)
        output = "[Square] (28) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq2 = Square(5)
        output = "[Square] (29) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq2)
            self.assertEqual(out.getvalue(), output)
        dct = sq.to_dictionary()
        sq2.update(**dct)
        self.assertEqual(sq.width, sq2.width)
        self.assertEqual(sq.height, sq2.height)
        self.assertEqual(sq.x, sq2.x)
        self.assertEqual(sq.y, sq2.y)
        self.assertEqual(sq.id, sq2.id)
        output = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(type(dct))
            self.assertEqual(out.getvalue(), output)

    def test_14value_square(self):
        """ Test value passed to Square """
        with self.assertRaises(ValueError):
            Square(-1)

    def test_15create(self):
        """ Test create method """
        dictionary = {'id': 89}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 89)
        dictionary = {'id': 89, 'size': 1}
        sq = Rectangle.create(**dictionary)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        dictionary = {'id': 89, 'size': 1, 'x': 2}
        sq = Rectangle.create(**dictionary)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        sq = Rectangle.create(**dictionary)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)

    def test_16save_to_file(self):
        """ Test JSON file """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        sq = Square(2, 2)
        Square.save_to_file([sq])
        output = '[{\"id\": 34, '
        output += '\"size\": 2, \"x\": 2, \"y\": 0}]'
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), output)
