#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_pass(self):
        self.none(max_integer([]), None)
        self.allminus(max_integer([-1, -2, -3, -4]), -1)
        self.oneminus(max_integer([1, 2, 3, -4]), 3)
   # def test_negative(self):
        #self.test1(ValueError, max_integer, msg="Only negative numbers in the list")
