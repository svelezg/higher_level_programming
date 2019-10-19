#!/usr/bin/python3
"""
Unittest for Rectangle class
"""

import unittest
import contextlib
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_classBase(self):
        r0 = Rectangle(1, 1)
        self.assertIsInstance(r0, Base)
        self.assertIsInstance(r0, Rectangle)

    def test_class(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(isinstance(r0, Base))

    def test_subclass(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(isinstance(r0, Rectangle))

    def test_nb(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, '_Base__nb_objects'))
        Base._Base__nb_objects = 0

    def test_rectangle_arg(self):
        self.assertRaises(TypeError, Rectangle)
        #self.assertRaisesRegex(TypeError,
         #                      "__init__() missing 2 required positional arguments: 'width' and 'height'",
          #                     Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        #self.assertRaisesRegex(TypeError,
         #                      "__init__() missing 1 required positional argument: 'height'",
           #                     Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, 1, 1, 1)
        #self.assertRaisesRegex(TypeError,
         #                      "__init__() takes from 3 to 6 positional arguments but 7 were given",
          #                     Rectangle, 1, 1, 1, 1, 1)
        Base._Base__nb_objects = 0

    def test_id(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'id'))
        Base._Base__nb_objects = 0

    def test_width(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'width'))
        Base._Base__nb_objects = 0

    def test_width_value(self):
        r0 = Rectangle(1, 1)
        self.assertEqual(r0.width, 1)
        Base._Base__nb_objects = 0

    def test_width_string(self):
        self.assertRaises(TypeError, Rectangle, "string", 1)
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, "string", 1)
        Base._Base__nb_objects = 0

    def test_width_neg(self):
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, -1, 1)
        Base._Base__nb_objects = 0

    def test_height(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'height'))
        Base._Base__nb_objects = 0

    def test_height_value(self):
        r0 = Rectangle(1, 1)
        self.assertEqual(r0.height, 1)
        Base._Base__nb_objects = 0

    def test_height_string(self):
        self.assertRaises(TypeError, Rectangle, 1, "string")
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 1, "string")
        Base._Base__nb_objects = 0

    def test_height_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 1, -1)
        Base._Base__nb_objects = 0

    def test_x(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'x'))
        Base._Base__nb_objects = 0

    def test_x_value(self):
        r0 = Rectangle(1, 1, 1)
        self.assertEqual(r0.x, 1)
        Base._Base__nb_objects = 0

    def test_x_string(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "x must be an integer", Rectangle, 1, 1, "string")
        Base._Base__nb_objects = 0

    def test_x_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "x must be >= 0", Rectangle, 1, 1, -1)
        Base._Base__nb_objects = 0

    def test_y(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'y'))
        Base._Base__nb_objects = 0

    def test_y_value(self):
        r0 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r0.y, 1)
        Base._Base__nb_objects = 0

    def test_y_string(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "y must be an integer", Rectangle, 1, 1, 1,"string")
        Base._Base__nb_objects = 0

    def test_y_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "y must be >= 0", Rectangle, 1, 1, 1, -1)
        Base._Base__nb_objects = 0

    def test_automatic(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(1, 1)
        self.assertEqual(r4.id, 4)
        r5 = Rectangle(1, 1)
        self.assertEqual(r5.id, 5)
        Base._Base__nb_objects = 0

    def test_manual(self):
        r1 = Rectangle(1, 1, 0, 0, 45)
        self.assertEqual(r1.id, 45)
        r2 = Rectangle(1, 1, 0, 0, 56)
        self.assertEqual(r2.id, 56)
        r3 = Rectangle(1, 1, 0, 0, 67)
        self.assertEqual(r3.id, 67)
        r4 = Rectangle(1, 1, 0, 0, 78)
        self.assertEqual(r4.id, 78)
        r5 = Rectangle(1, 1, 0, 0, 89)
        self.assertEqual(r5.id, 89)
        Base._Base__nb_objects = 0

    def test_mixed(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 1, 0, 0, 56)
        self.assertEqual(r2.id, 56)
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.id, 2)
        r4 = Rectangle(1, 1, 0, 0, 78)
        self.assertEqual(r4.id, 78)
        r5 = Rectangle(1, 1)
        self.assertEqual(r5.id, 3)
        Base._Base__nb_objects = 0

    def test_area(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'area'))
        Base._Base__nb_objects = 0

    def test_area_value(self):
        r0 = Rectangle(1, 1)
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r0.area(), 1)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
        Base._Base__nb_objects = 0

    def test_display(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'display'))
        Base._Base__nb_objects = 0

    def test_display(self):
        string = "##\n##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Rectangle(2, 2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        string = "####\n####\n####\n####\n####\n####"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Rectangle(4, 6).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display1(self):
        string = "+\n\n  ##\n  ##\n  ##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Rectangle(2, 3, 2, 2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_display2(self):
        string = "+ ###\n ###"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Rectangle(3, 2, 1, 0).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display_arg(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertRaises(TypeError, r1.display, 1)
        #self.assertRaisesRegex(TypeError,
         #                      'display() takes 1 positional argument but 2 were given',
          #                     r1.display, 1)
        Base._Base__nb_objects = 0

    def test_str(self):
        string = "[Rectangle] (1) 0/0 - 1/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(1, 1,)
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Rectangle] (12) 2/1 - 4/6"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Rectangle] (1) 1/0 - 5/5"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r2 = Rectangle(5, 5, 1)
            print(r2)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_uptdate(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        string = "[Rectangle] (89) 10/10 - 10/10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2)
        string = "[Rectangle] (89) 10/10 - 2/10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3)
        string = "[Rectangle] (89) 10/10 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3, 4)
        string = "[Rectangle] (89) 4/10 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        r1.update(89, 2, 3, 4, 5)
        string = "[Rectangle] (89) 4/5 - 2/3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
