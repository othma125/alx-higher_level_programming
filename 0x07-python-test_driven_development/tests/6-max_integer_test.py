#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unitest for max_integer([..]).
    """

    def test_equal(self):
        """
        all possible equal tests
        :return:git
        :rtype:
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(list(range(10))), 9)
        self.assertEqual(max_integer([9, 1, 0, -19, 19]), 19)
        self.assertEqual(max_integer([14.2, 26.1, 9]), 26.1)
        self.assertEqual(max_integer(''), None)
        self.assertEqual(max_integer('I love Python'), 'y')
        self.assertEqual(max_integer(['I', 'love', 'Python']), 'love')


if __name__ == '__main__':
    unittest.main()
