#!/usr/bin/python3
""" Module for test Base class """
import unittest


from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square
from unittest import TestCase


# from unittest.mock import patch


class TestBaseMethods(TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base.__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        b = Base(1)
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        b2 = Base(1024)
        b3 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 1024)
        self.assertEqual(b3.id, 3)
        b = Base()
        self.assertEqual(b.id, 4)
        b = Base()
        self.assertEqual(b.id, 5)
        b = Base()
        self.assertEqual(b.id, 6)

    def test_string_id(self):
        """ Test string id """
        b = Base('1')
        self.assertEqual(b.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        with self.assertRaises(AttributeError):
            Base.nb_objects
