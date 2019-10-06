#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([1]), 1)

    def test_one_neg(self):
        self.assertEqual(max_integer([-11]), -11)

    def test_neg(self):
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

    def test_middle(self):
        self.assertEqual(max_integer([1, 3, 8, 2, 6]), 8)

if __name__ == '__main__':
    unittest.main()
