#!/usr/bin/python3
import unittest
import json
import sys
import io
import pep8
from models import square
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareDocs(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(square.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Square.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Square):
            self.assertTrue(len(func.__doc__) > 0)


class TestSquarePep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test square and test_square for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/square.py'
        file2 = 'tests/test_models/test_square.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestSquare(unittest.TestCase):
    """ tests for class Square """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        Base._Base__nb_objects = 0
        cls.s1 = Square(10)
        cls.s2 = Square(5, 5)
        cls.s3 = Square(1, 2, 3)
        cls.s4 = Square(4, 5, 6, 7)

    def test_id(self):
        """ test id attribute """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 7)

    def test_size(self):
        """ test size attribute """
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 5)
        self.assertEqual(self.s3.size, 1)
        self.assertEqual(self.s4.size, 4)

    def test_x(self):
        """ test x attribute """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 5)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s4.x, 5)

    def test_y(self):
        """ test y attribute """
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.y, 6)

    def test_area(self):
        """ test area method """
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 25)
        self.assertEqual(self.s3.area(), 1)
        self.assertEqual(self.s4.area(), 16)

    def test_str(self):
        """ test __str__ method """
        self.assertEqual(str(self.s1), '[Square] (1) 0/0 - 10')
        self.assertEqual(str(self.s2), '[Square] (2) 5/0 - 5')
        self.assertEqual(str(self.s3), '[Square] (3) 2/3 - 1')
        self.assertEqual(str(self.s4), '[Square] (7) 5/6 - 4')

    def test_dictionary(self):
        """ test to_dictionary method """
        d1 = self.s1.to_dictionary()
        self.assertDictEqual(d1, {'size': 10, 'x': 0,
                                  'id': 1, 'y': 0})
        d2 = self.s2.to_dictionary()
        self.assertDictEqual(d2, {'size': 5, 'x': 5,
                                  'y': 0, 'id': 2})
        d3 = self.s3.to_dictionary()
        self.assertDictEqual(d3, {'size': 1, 'x': 2,
                                  'id': 3, 'y': 3})
        d4 = self.s4.to_dictionary()
        self.assertDictEqual(d4, {'id': 7, 'x': 5, 'y': 6,
                                  'size': 4})

    def test_size__errors(self):
        """ test size type and value errors """
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s = Square(-1)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s = Square("one")
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s = Square(1.1)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s = Square({1: 2})
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s = Square((1, 2))
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s = Square([1, 2])

    def test_x_errors(self):
        """ test x type and value errors """
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s = Square(1, -2)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s = Square(1, "two")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s = Square(1, 2.2)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s = Square(1, {2: 3})
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s = Square(1, (2, 3))
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s = Square(1, [2, 3])

    def test_y_errors(self):
        """ test y type and value errors """
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s = Square(1, 2, -3)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s = Square(1, 2, "three")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s = Square(1, 2, 3.3)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s = Square(1, 2, {3: 4})
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s = Square(1, 2, (3, 4))
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s = Square(1, 2, [3, 4])

    def test_update_args(self):
        """ test update method using no-keyword arguments """
        s = Square(1, 1, 1, 1)
        self.assertEqual(str(s), '[Square] (1) 1/1 - 1')
        s.update(2)
        self.assertEqual(str(s), '[Square] (2) 1/1 - 1')
        s.update(2, 3)
        self.assertEqual(str(s), '[Square] (2) 1/1 - 3')
        s.update(2, 3, 4)
        self.assertEqual(str(s), '[Square] (2) 4/1 - 3')
        s.update(2, 3, 4, 5)
        self.assertEqual(str(s), '[Square] (2) 4/5 - 3')

    def test_update_kwargs(self):
        """ test update method using keyword arguments """
        s = Square(1, 1, 1, 1)
        self.assertEqual(str(s), '[Square] (1) 1/1 - 1')
        s.update(id=2)
        self.assertEqual(str(s), '[Square] (2) 1/1 - 1')
        s.update(size=3)
        self.assertEqual(str(s), '[Square] (2) 1/1 - 3')
        s.update(x=5, y=6)
        self.assertEqual(str(s), '[Square] (2) 5/6 - 3')
        s.update(id=10, size=10, x=10, y=10)
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')

    def test_simple_display(self):
        """ test display with size only (no x and y) """
        saved_stdout = sys.stdout
        s = Square(2)
        out = io.StringIO()
        sys.stdout = out
        s.display()
        output = out.getvalue()
        self.assertEqual(output, "##\n##\n")
        sys.stdout = saved_stdout

    def test_complex_display(self):
        """ test display with size, x, and y attributes """
        saved_stdout = sys.stdout
        s = Square(2, 1, 1)
        out = io.StringIO()
        sys.stdout = out
        s.display()
        output = out.getvalue()
        self.assertEqual(output, "\n ##\n ##\n")
        sys.stdout = saved_stdout

    def test_arg_errors(self):
        """ test cases with too few/too many arguments """
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            self.s1.display(1)
        with self.assertRaises(TypeError):
            self.s1.to_dictionary(1)
        with self.assertRaises(TypeError):
            self.s1.area(1)

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
