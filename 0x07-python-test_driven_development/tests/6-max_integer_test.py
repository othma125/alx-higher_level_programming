#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unitest for max_integer([..]).
    """
    def EqualTest(self):
        """
        all possible equal tests
        :return:git
        :rtype:
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(list(range(10))), 9)
        self.assertEqual(max_integer([4.2, 29.8, 9]), 29.8)
        self.assertEqual(max_integer(''), None)
        self.assertEqual(max_integer('I love Python'), 'y')
        self.assertEqual(max_integer(['I', 'love', 'Python']), 'love')


if __name__ == '__main__':
    unittest.main()
