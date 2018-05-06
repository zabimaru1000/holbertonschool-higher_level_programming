#!/usr/bin/python3
"""
Module for matrix_divided
Uses one function divide all integers in 2D list
"""


def matrix_divided(matrix, div):
    """
    Returns result of all ints divided by div
    """

    result = [[round(i / div, 2) for i in j] for j in matrix]

    return result
