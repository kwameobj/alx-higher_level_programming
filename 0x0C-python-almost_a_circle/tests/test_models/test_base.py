#!/usr/bin/python3
import unittest
import json
import sys
import io
import pep8
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseDocs(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


class TestBasePep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBase(unittest.TestCase):
    """ tests for class Base """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(98)
        cls.b4 = Base()
        cls.b5 = Base("five")
        cls.b6 = Base(6.6)
        cls.r1 = Rectangle(1, 1, 0, 0, 1)

    def test_id(self):
        """ test id attribute """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 98)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b5.id, "five")
        self.assertEqual(self.b6.id, 6.6)

    def test_to_json(self):
        """ test to_json_string method """
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        d1 = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}
        json_test = Base.to_json_string(d1)
        self.assertTrue(type(json_test) is str)
        test_dict = json.loads(json_test)
        self.assertEqual(test_dict, d1)

    def test_from_json(self):
        """ test from_json_string method """
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.from_json_string(None), [])

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
