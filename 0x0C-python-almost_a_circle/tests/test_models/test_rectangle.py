#!/usr/bin/python3
import unittest
import json
import sys
import io
import pep8
from models import rectangle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleDocs(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)


class TestRectanglePep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test rectangle and test_rectangle for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/rectangle.py'
        file2 = 'tests/test_models/test_rectangle.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestRectangle(unittest.TestCase):
    """ tests for class Rectangle """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(5, 5, 5)
        cls.r3 = Rectangle(1, 2, 3, 4)
        cls.r4 = Rectangle(5, 6, 7, 8, 9)

    def test_id(self):
        """ test id attribute """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 9)

    def test_width(self):
        """ test width attribute """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r4.width, 5)

    def test_height(self):
        """ test height attribute """
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r4.height, 6)

    def test_x(self):
        """ test x attribute """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 5)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r4.x, 7)

    def test_y(self):
        """ test y attribute """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 4)
        self.assertEqual(self.r4.y, 8)

    def test_area(self):
        """ test area method """
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 25)
        self.assertEqual(self.r3.area(), 2)
        self.assertEqual(self.r4.area(), 30)

    def test_str(self):
        """ test __str__ method """
        self.assertEqual(str(self.r1), '[Rectangle] (1) 0/0 - 10/10')
        self.assertEqual(str(self.r2), '[Rectangle] (2) 5/0 - 5/5')
        self.assertEqual(str(self.r3), '[Rectangle] (3) 3/4 - 1/2')
        self.assertEqual(str(self.r4), '[Rectangle] (9) 7/8 - 5/6')

    def test_dictionary(self):
        """ test to_dictionary method """
        d1 = self.r1.to_dictionary()
        self.assertDictEqual(d1, {'height': 10, 'x': 0,
                                  'id': 1, 'y': 0, 'width': 10})
        d2 = self.r2.to_dictionary()
        self.assertDictEqual(d2, {'width': 5, 'x': 5,
                                  'y': 0, 'id': 2, 'height': 5})
        d3 = self.r3.to_dictionary()
        self.assertDictEqual(d3, {'width': 1, 'x': 3,
                                  'height': 2, 'id': 3, 'y': 4})
        d4 = self.r4.to_dictionary()
        self.assertDictEqual(d4, {'id': 9, 'x': 7, 'y': 8,
                                  'height': 6, 'width': 5})

    def test_width__errors(self):
        """ test width type and value errors """
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(-1, 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle("one", 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(1.1, 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle({1: 2}, 3)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle((1, 2), 3)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle([1, 2], 3)

    def test_height_errors(self):
        """ test height type and value errors """
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r = Rectangle(1, -2)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r = Rectangle(1, "two")
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r = Rectangle(1, 2.2)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r = Rectangle(1, {2: 3})
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r = Rectangle(1, (2, 3))
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r = Rectangle(1, [2, 3])

    def test_x_errors(self):
        """ test x type and value errors """
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r = Rectangle(1, 2, -3, 4)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(1, 2, "three", 4)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(1, 2, 3.3, 4)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(1, 2, {3: 4}, 5)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(1, 2, (3, 4), 5)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(1, 2, [3, 4], 5)

    def test_y_errors(self):
        """ test y type and value errors """
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r = Rectangle(1, 2, 3, -4)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(1, 2, 3, "four")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(1, 2, 3, 4.4)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(1, 2, 3, {4: 5})
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(1, 2, 3, (4, 5))
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(1, 2, 3, [4, 5])

    def test_update_args(self):
        """ test update method using no-keyword arguments """
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(r), '[Rectangle] (1) 1/1 - 1/1')
        r.update(2)
        self.assertEqual(str(r), '[Rectangle] (2) 1/1 - 1/1')
        r.update(2, 3)
        self.assertEqual(str(r), '[Rectangle] (2) 1/1 - 3/1')
        r.update(2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (2) 1/1 - 3/4')
        r.update(2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (2) 5/1 - 3/4')
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(str(r), '[Rectangle] (2) 5/6 - 3/4')

    def test_update_kwargs(self):
        """ test update method using keyword arguments """
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(r), '[Rectangle] (1) 1/1 - 1/1')
        r.update(id=2)
        self.assertEqual(str(r), '[Rectangle] (2) 1/1 - 1/1')
        r.update(width=3)
        self.assertEqual(str(r), '[Rectangle] (2) 1/1 - 3/1')
        r.update(height=4)
        self.assertEqual(str(r), '[Rectangle] (2) 1/1 - 3/4')
        r.update(x=5, y=6)
        self.assertEqual(str(r), '[Rectangle] (2) 5/6 - 3/4')
        r.update(id=10, height=10, width=10, x=10, y=10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')

    def test_simple_display(self):
        """ test display with width and height only (no x and y) """
        saved_stdout = sys.stdout
        r = Rectangle(2, 2)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        output = out.getvalue()
        self.assertEqual(output, "##\n##\n")
        sys.stdout = saved_stdout

    def test_complex_display(self):
        """ test display with width, height, x, and y attributes """
        saved_stdout = sys.stdout
        r = Rectangle(2, 2, 1, 1)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        output = out.getvalue()
        self.assertEqual(output, "\n ##\n ##\n")
        sys.stdout = saved_stdout

    def test_arg_errors(self):
        """ test cases with too few/too many arguments """
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            self.r1.display(1)
        with self.assertRaises(TypeError):
            self.r1.to_dictionary(1)
        with self.assertRaises(TypeError):
            self.r1.area(1)

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
