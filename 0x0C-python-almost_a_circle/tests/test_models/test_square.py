#!/usr/bin/python3
""" Module for test Square class """
from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base.__nb_objects = 0

    def tearDown(self):
        """ Method invoked for each test """
        Base.__nb_objects = 0

    def test_square_01_new_square(self):
        """ Test new square """
        Base._Base__nb_objects = 0
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

    def test_square_02_new_squares(self):
        """ Test new squares """
        Base._Base__nb_objects = 0
        sq = Square(1, 1)
        self.assertIsNot(sq, Square(1, 1))
        self.assertFalse(sq.id == Square(1, 1).id)

    def test_square_03_is_Base_instance(self):
        """ Test Square is a Base instance """
        Base._Base__nb_objects = 0
        self.assertIsInstance(Square(1), Base)

    def test_square_04_is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """
        Base._Base__nb_objects = 0
        self.assertIsInstance(Square(1), Rectangle)

    def test_square_05_incorrect_amount_attrs(self):
        """ Test error raise with no args passed """
        Base._Base__nb_objects = 0
        output = '__init__() missing 1 required'
        output += " positional argument: 'size'"
        with self.assertRaises(TypeError) as e:
            Square()
        self.assertEqual(str(e.exception), output)
        output = 'Square.__init__() takes from 2 to 5'
        output += " positional arguments but 6 were given"
        with self.assertRaises(TypeError) as e:
            Square(1, 1, 1, 1, 1)
        self.assertEqual(str(e.exception), output)

    def test_square_06_access_private_attrs(self):
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

    def test_square_07_valid_attrs(self):
        """ Trying to pass a string value """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError) as e:
            Square("2", 2, 2, 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            Square(2, "2", 2, 2)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            Square(2, 2, "2", 2)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_square_08_value_attrs(self):
        """ Trying to pass invalid values """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            Square(1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            Square(1, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_square_09_area(self):
        """ Checking the return value of area method """
        Base._Base__nb_objects = 0
        sq = Square(4)
        self.assertEqual(sq.area(), 16)
        sq = Square(2)
        self.assertEqual(sq.area(), 4)
        sq.size = 5
        self.assertEqual(sq.area(), 25)

    def test_square_10_display(self):
        """ Test string printed """
        Base._Base__nb_objects = 0
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
        output = "[Square] (3) 2/2 - 4\n"
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

    def test_square_11_str(self):
        """ Test __str__ return value """
        Base._Base__nb_objects = 0
        sq = Square(5)
        output = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        s2 = Square(3, 7, 1)
        output = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(s2)
            self.assertEqual(out.getvalue(), output)
        sq = Square(1, 1, 1)
        output = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq = Square(3)
        output = "[Square] (4) 0/0 - 3"
        self.assertEqual(str(sq), output)

    def test_square_12_update(self):
        """ Test update method """
        Base._Base__nb_objects = 0
        sq = Square(3)
        output = "[Square] (1) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq.update(5)
        output = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq = Square(3)
        output = "[Square] (2) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq.update(5)
        output = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), output)
        sq = Square(1)
        output = "[Square] (3) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq.update(2, 2, 2, 2)
        output = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq.update(y=3)
        output = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq.update(id=1, size=10)
        output = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq = Square(10)
        output = "[Square] (4) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        dic = {'size': 3, 'y': 5}
        sq.update(**dic)
        output = "[Square] (4) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq = Square(7)
        output = "[Square] (5) 0/0 - 7\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        dic = {'id': 10, 'x': '5', 'y': 5}
        with self.assertRaises(TypeError):
            sq.update(**dic)

    def test_square_13_to_dictionary(self):
        """ Test dictionary returned """
        Base._Base__nb_objects = 0
        sq = Square(1, 2, 3)
        output = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.width, 1)
        self.assertEqual(sq.height, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 1)
        output = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(type(sq.to_dictionary()))
            self.assertEqual(out.getvalue(), output)
        sq = Square(2, 2, 2)
        output = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as out:
            print(sq)
            self.assertEqual(out.getvalue(), output)
        sq2 = Square(5)
        output = "[Square] (3) 0/0 - 5\n"
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

    def test_square_14_value_square(self):
        """ Test value passed to Square """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_15_create(self):
        """ Test create method """
        Base._Base__nb_objects = 0
        dictionary = {'id': 89}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 89)
        dictionary = {'id': 89, 'size': 1}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        dictionary = {'id': 89, 'size': 1, 'x': 2}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)

    def test_square_16_save_to_file(self):
        """ Test JSON file """
        Base._Base__nb_objects = 0
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        sq = Square(2, 2)
        Square.save_to_file([sq])
        output = '[{\"id\": 1, '
        output += '\"size\": 2, \"x\": 2, \"y\": 0}]'
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), output)

    def test_square_17_from_json_string(self):
        """ Test JSON file """
        Base._Base__nb_objects = 0
        list_input = [
            {"size": 4, "id": 89},
            {"size": 7, "id": 7}
        ]
        output = '[<class \'list\'>] '
        output += f'[{list_input[0]}, '
        output += f'{list_input[1]}]\n'
        with patch('sys.stdout', new=StringIO()) as out:
            print(f"[{type(list_input)}] {list_input}")
            self.assertEqual(out.getvalue(), output)
        json_list_input = Square.to_json_string(list_input)
        output = '[<class \'str\'>] '
        output += '[{\"size\": 4, \"id\": 89}, '
        output += '{\"size\": 7, \"id\": 7}]\n'
        with patch('sys.stdout', new=StringIO()) as out:
            print(f"[{type(json_list_input)}] {json_list_input}")
            self.assertEqual(out.getvalue(), output)
        list_output = Square.from_json_string(json_list_input)
        output = '[<class \'list\'>] '
        output += f'[{list_output[0]}, '
        output += f'{list_output[1]}]\n'
        with patch('sys.stdout', new=StringIO()) as out:
            print(f"[{type(list_output)}] {list_output}")
            self.assertEqual(out.getvalue(), output)

    def test_square_18_load_from_file(self):
        """ Test load JSON file """
        Base._Base__nb_objects = 0
        load_file = Square.load_from_file()
        self.assertEqual(type(load_file), list)
        r1 = Square(5, 5)
        r2 = Square(8, 2, 5, 5)
        inputs = [r1, r2]
        Square.save_to_file(inputs)
        outputs = Square.load_from_file()
        for r, rr in zip(inputs, outputs):
            self.assertEqual(str(r), str(rr))

    def test_square_19_csv(self):
        """ Test csv file """
        Base._Base__nb_objects = 0
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), 'id,size,x,y\n')
        Square.save_to_file([])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), 'id,size,x,y\n')
        sq = Square(2, 2)
        Square.save_to_file_csv([sq])
        output = 'id,size,x,y\n1,2,2,0\n'
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), output)
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), output)
        list_sq = Square.load_from_file_csv()
        output = '[Square] (1) 2/0 - 2\n'
        with patch('sys.stdout', new=StringIO()) as out:
            for sq in list_sq:
                print(sq)
            self.assertEqual(out.getvalue(), output)


if __name__ == "__main__":
    main()
