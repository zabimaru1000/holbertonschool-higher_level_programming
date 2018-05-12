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

    def misc_test(self):
        """
        Test to check arguments that are not a positive integer.
        """
        result = max_integer([])
        self.assertEqual(result, None)
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)
        result = max_integer([1, 2, 3, -4])
        self.assertEqual(result, 3)

    if __name__ == "__main__":
        unittest.main()
