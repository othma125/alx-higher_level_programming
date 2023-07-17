#!/usr/bin/python3
""" Module for test Rectangle class """
from io import StringIO
from json import dumps
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_rectangle_01_new_rectangle(self):
        """ Test new rectangle """
        Base._Base__nb_objects = 0
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
        self.assertIsNot(r, Rectangle(1, 1))
        self.assertFalse(r.id == Rectangle(1, 1).id)
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)
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

    def test_rectangle_02_incorrect_amount_attrs(self):
        """ Test error raise with no enough arguments passed """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_03_access_private_attrs(self):
        """ Trying to access to a private attribute """
        Base._Base__nb_objects = 0
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

    def test_rectangle_04_valid_attrs(self):
        """ Trying to pass a string value """
        Base._Base__nb_objects = 0
        output = 'Rectangle.__init__() takes from 3 to 6'
        output += " positional arguments but 7 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle(2, 3, 2, 2, 2, 2)
        self.assertEqual(str(e.exception), output)
        with self.assertRaises(TypeError) as e:
            Rectangle("2", 2, 2, 2, 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(2, "2", 2, 2, 2)
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(2, 2, "2", 2, 2)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(2, 2, 2, "2", 2)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_rectangle_05_value_attrs(self):
        """ Trying to pass invalid values """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 1)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_rectangle_06_display(self):
        """ Test string printed """
        Base._Base__nb_objects = 0
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

    def test_rectangle_07_str(self):
        """ Test __str__ return value """
        Base._Base__nb_objects = 0
        r = Rectangle(2, 5, 2, 4)
        output = "[Rectangle] (1) 2/4 - 2/5\n"
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
        output = "[Rectangle] (2) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(25, 86, 4, 7)
        output = "[Rectangle] (3) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(1, 1, 1, 1)
        output = "[Rectangle] (4) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r = Rectangle(3, 3)
        output = "[Rectangle] (5) 0/0 - 3/3"
        self.assertEqual(str(r), output)

    def test_rectangle_08_to_dictionary(self):
        """ Test dictionary returned """
        Base._Base__nb_objects = 0
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
        output = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), output)
        r2 = Rectangle(5, 7)
        output = "[Rectangle] (2) 0/0 - 5/7\n"
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

    def test_rectangle_09_check_value(self):
        """ Test args passed """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_10_create(self):
        """ Test create method """
        Base._Base__nb_objects = 0
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

    def test_rectangle_11_dict_to_json(self):
        """ Test Dictionary to JSON string """
        Base._Base__nb_objects = 0
        r = Rectangle(2, 2)
        dictionary = r.to_dictionary()
        output = f"[{dumps(dictionary)}]\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(Base.to_json_string([dictionary]))
            self.assertEqual(out.getvalue(), output)

    def test_rectangle_12_save_to_file(self):
        """ Test JSON file """
        Base._Base__nb_objects = 0
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        r = Rectangle(2, 2)
        Rectangle.save_to_file([r])
        output = '[{\"x\": 0, '
        output += '\"width\": 2, \"id\": 1, \"height\": 2, \"y\": 0}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), output)

    def test_rectangle_13_from_json_string(self):
        """ Test JSON file """
        Base._Base__nb_objects = 0
        list_input = [
            {'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ]
        output = '[<class \'list\'>] '
        output += '[{\'height\': 4, \'width\': 10, \'id\': 89}, '
        output += '{\'height\': 7, \'width\': 1, \'id\': 7}]'
        with patch('sys.stdout', new=StringIO()) as out:
            print(f"[{type(list_input)}] {list_input}", end='')
            self.assertEqual(out.getvalue(), output)
        json_list_input = Rectangle.to_json_string(list_input)
        output = '[<class \'str\'>] '
        output += '[{\"height\": 4, \"width\": 10, \"id\": 89}, '
        output += '{\"height\": 7, \"width\": 1, \"id\": 7}]'
        with patch('sys.stdout', new=StringIO()) as out:
            print(f"[{type(json_list_input)}] {json_list_input}", end='')
            self.assertEqual(out.getvalue(), output)
        list_output = Rectangle.from_json_string(json_list_input)
        output = '[<class \'list\'>] '
        output += '[{\'height\': 4, \'width\': 10, \'id\': 89}, '
        output += '{\'height\': 7, \'width\': 1, \'id\': 7}]'
        with patch('sys.stdout', new=StringIO()) as out:
            print(f"[{type(list_output)}] {list_output}", end='')
            self.assertEqual(out.getvalue(), output)

    def test_rectangle_14_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(type(load_file), list)
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)
        inputs = [r1, r2]
        Rectangle.save_to_file(inputs)
        outputs = Rectangle.load_from_file()
        for r, rr in zip(inputs, outputs):
            self.assertEqual(str(r), str(rr))

    def test_rectangle_15_csv(self):
        """ Test csv file """
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), 'id,width,height,x,y\n')
        Rectangle.save_to_file([])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), 'id,width,height,x,y\n')
        r = Rectangle(2, 2)
        Rectangle.save_to_file_csv([r])
        output = 'id,width,height,x,y\n1,2,2,0,0\n'
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), output)
        list_rec = Rectangle.load_from_file_csv()
        output = '[Rectangle] (1) 0/0 - 2/2\n'
        with patch('sys.stdout', new=StringIO()) as out:
            for r in list_rec:
                print(r)
            self.assertEqual(out.getvalue(), output)
