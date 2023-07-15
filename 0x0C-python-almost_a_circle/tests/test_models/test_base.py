#!/usr/bin/python3
""" Module for test Base class """


from models.base import Base
from unittest import TestCase


class TestBaseMethods(TestCase):
    """ Suite to test Base class """

    # def setUp(self):
    #     """ Method invoked for each test """
    #     Base.nb_objects(0)

    # def tearDown(self):
    #     """ Method invoked for each test """
    #     Base.__nb_objects = 7

    def test_base_00_id(self):
        """ Test assigned id """
        b = Base(10)
        self.assertEqual(b.id, 10)
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        b2 = Base(1024)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1024)
        self.assertEqual(b3.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_base_01_string_id(self):
        """ Test string id """
        b = Base('1')
        self.assertEqual(b.id, '1')

    def test_base_02_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_base_03_access_private_attrs(self):
        """ Test accessing to private attributes """
        with self.assertRaises(AttributeError):
            Base.nb_objects
