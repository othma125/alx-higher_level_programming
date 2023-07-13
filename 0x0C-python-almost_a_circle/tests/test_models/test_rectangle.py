#!/usr/bin/python3
""" Module for test Rectangle class """
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base.__nb_objects = 0

    def test_01new_rectangle(self):
        """ Test new rectangle """
        r = Rectangle(1, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)
        r = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 4)
        r = Rectangle(1, 1)
        self.assertFalse(r is Rectangle(1, 1))
        self.assertFalse(r.id == Rectangle(1, 1).id)
        r = Rectangle(1, 1)
        self.assertTrue(isinstance(r, Base))
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)
        r.width = 5
        self.assertEqual(r.area(), 10)
        r.height = 5
        self.assertEqual(r.area(), 25)
        r = Rectangle(3, 8)
        self.assertEqual(r.area(), 24)
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)

    def test_02incorrect_amount_attrs(self):
        """ Test error raise with no enough arguments passed """
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_03access_private_attrs(self):
        """ Trying to access to a private attribute """
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__width
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__height
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__x
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__y

    def test_07valid_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            Rectangle("2", 2, 2, 2, 2)
        with self.assertRaises(TypeError):
            Rectangle(2, "2", 2, 2, 2)
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "2", 2, 2)
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 2, "2", 2)

    def test_08value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_09display(self):
        """ Test string printed """
        r = Rectangle(2, 5)
        output = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(2, 2)
        output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)
        r.width = 5
        output = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(5, 4, 1, 1)
        output = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(3, 2)
        output = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)
        r.x = 4
        output = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)
        r.y = 2
        output = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)

    def test_10str(self):
        """ Test __str__ return value """
        r = Rectangle(2, 5, 2, 4)
        output = "[Rectangle] (18) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(3, 2, 8, 8, 10)
        output = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r.id = 1
        r.width = 7
        r.height = 15
        output = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(5, 10)
        output = "[Rectangle] (19) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(25, 86, 4, 7)
        output = "[Rectangle] (20) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(1, 1, 1, 1)
        output = "[Rectangle] (21) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(3, 3)
        output = "[Rectangle] (22) 0/0 - 3/3"
        self.assertEqual(r.__str__(), output)

    def test_11to_dictionary(self):
        """ Test dictionary returned """
        r = Rectangle(1, 2, 3, 4, 1)
        output = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1)
        output = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(type(r.to_dictionary()))
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(2, 2, 2, 2)
        output = "[Rectangle] (23) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r2 = Rectangle(5, 7)
        output = "[Rectangle] (24) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r2)
            self.assertEqual(out.getvalue(), output)
        r1_dictionary = r.to_dictionary()
        r2.update(**r1_dictionary)
        self.assertEqual(r.width, r2.width)
        self.assertEqual(r.height, r2.height)
        self.assertEqual(r.x, r2.x)
        self.assertEqual(r.y, r2.y)
        self.assertEqual(r.id, r2.id)
        output = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), output)

    def test_13check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_14check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_15create(self):
        """ Test create method """
        dictionary = {'id': 89, 'height': 17}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.height, 17)
        dictionary = {'id': 89, 'width': 1}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    # def test_16load_from_file(self):
    #     """ Test load JSON file """
    #     load_file = Rectangle.load_from_file()
    #     self.assertEqual(load_file, [])
    #     r1 = Rectangle(5, 5)
    #     r2 = Rectangle(8, 2, 5, 5)
    #     linput = [r1, r2]
    #     Rectangle.save_to_file(linput)
    #     loutput = Rectangle.load_from_file()
    #     for i in range(len(linput)):
    #         self.assertEqual(linput[i].__str__(), loutput[i].__str__())

    # def test_17dict_to_json(self):
    #     """ Test Dictionary to JSON string """
    #     r1 = Rectangle(2, 2)
    #     dictionary = r1.to_dictionary()
    #     json_dictionary = Base.to_json_string([dictionary])
    #     res = "[{}]\n".format(dictionary.__str__())
    #
    #     with patch('sys.stdout', new=StringIO()) as str_out:
    #         print(json_dictionary)
    #         self.assertEqual(str_out.getvalue(), res.replace("'", "\""))
