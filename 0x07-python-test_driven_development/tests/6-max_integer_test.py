#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def normal_test(self):
        """
        Test to check if function works as intended.
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def empty_test(self):
        """
        Test to check arguments that are not a positive integer.
        """
        result = max_integer([])
        self.assertEqual(result, None)

    def allminus_test(self):
        """
        Tests all negative integers.
        """
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def minus_test(self):
        """
        Tests one negative integer.
        """
        result = max_integer([1, 2, 3, -4])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
