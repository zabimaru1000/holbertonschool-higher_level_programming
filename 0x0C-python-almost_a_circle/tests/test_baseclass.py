#!/usr/bin/python3
"""Unittest for class Base
"""


import unittest
from models.base import Base


class test_BaseModel(unittest.TestCase):
    def test_normal(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
