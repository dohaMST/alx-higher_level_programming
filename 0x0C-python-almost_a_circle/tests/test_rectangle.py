#!/usr/bin/python3
"""import unittest """
import unittest
from io import StringIO
from unittest import TestCase, mock
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """Test my class Square"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_empty(self):
        """Test if Rectangle constructor raises TypeError with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test if Rectangle constructor raises TypeError with one argument."""
        with self.assertRaises(TypeError):
            Rectangle(6)

    def test_many_arg(self):
        """Test if Rectangle constructor raises TypeError with too many args"""
        with self.assertRaises(TypeError):
            Rectangle(10, 32, 0, 0, 15, 61)

    def test_None(self):
        """Test if Rectangle constructor raises TypeError when passed None."""
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_no_id_or_none(self):
        """Test ID assignment when no ID or None passed to the constructor"""
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0).id, 1)
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0).id, 2)
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, None).id, 3)

    def test_id(self):
        """Test if the ID is correctly assigned when passed as an argument."""
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, 12).id, 12)
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, -2).id, -2)

    def test_private_getwidth_and_setwidth(self):
        """Test the private width attribute getter and setter."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width
        self.assertAlmostEqual(r.width, 1)
        r.width = 66
        self.assertAlmostEqual(r.width, 66)

    def test_private_getheight_and_setheight(self):
        """Test the private height attribute getter and setter."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__height
        self.assertAlmostEqual(r.height, 2)
        r.height = 55
        self.assertAlmostEqual(r.height, 55)

    def test_private_x_get_and_set(self):
        """Test the private x attribute getter and setter."""
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            r.__x
        self.assertAlmostEqual(r.x, 3)
        r.x = 678
        self.assertAlmostEqual(r.x, 678)

    def test_private_y_get_and_set(self):
        """Test the private y attribute getter and setter."""
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            r.__y
        self.assertAlmostEqual(r.y, 4)
        r.y = 100
        self.assertAlmostEqual(r.y, 100)

    def test_area(self):
        """Test the area() method."""
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, 1).area(), 6)
        self.assertAlmostEqual(Rectangle(6, 6, 0, 0, 1).area(), 36)

    def test_area_arg(self):
        """Test if area() method raises TypeError when passed an argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 0, 0, 1).area("test")

    def test_display_width_height(self):
        """Test the display() method with width and height."""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 4, 0, 0, 12).display()
            self.assertEqual(op.getvalue(), "###\n###\n###\n###\n")

    def test_display_width_x(self):
        """Test the display() method with width and x."""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 4, 2, 0, 12).display()
            self.assertEqual(op.getvalue(), "  ###\n  ###\n  ###\n  ###\n")

    def test_display_width_y(self):
        """Test the display() method with width and y."""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 4, 0, 2, 12).display()
            self.assertEqual(op.getvalue(), "\n\n###\n###\n###\n###\n")

    def test_display_width_arg(self):
        """Test if display() method raises TypeError when passed an arg"""
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 0, 2, 12).display(5)

    def test__str_normal(self):
        """Test the __str__ method with normal attributes."""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(Rectangle(4, 6, 2, 1, 12))

if __name__ == '__main__':
    unittest.main()
