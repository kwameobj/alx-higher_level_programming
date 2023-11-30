#!/usr/bin/python3
""" Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_import(self):
        self.assertTrue(__import__('6-max_integer').max_integer)

    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 9 , 8, 7]), 10)
        self.assertEqual(max_integer([10, 5, 20, 15]), 20)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-10, -9, -8]), -8)
        self.assertEqual(max_integer([1, -2, -3]), 1)

    def test_float(self):
        self.assertEqual(max_integer([1.65, 2.493, 3.1]), 3.1)
        self.assertEqual(max_integer([10.91, 9.12, 8.238]), 10.91)
        self.assertEqual(max_integer([10.34, 5.63, 20.001, 15.3]), 20.001)

    def test_words(self):
        self.assertEqual(max_integer(['hello', 'world', 'yellow']), 'yellow')

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_no_args(self):
        self.assertEqual(max_integer(), None)

    def test_non_int(self):
        with self.assertRaises(TypeError):
            max_integer(['A', 2, 3])

    def test_None(self):
        with self.assertRaises(TypeError):
            max_integer(None)
