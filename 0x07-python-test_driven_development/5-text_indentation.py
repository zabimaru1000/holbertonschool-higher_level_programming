#!/usr/bin/python3
"""
Module for text_indentation
Uses one function to split string by sentences
"""


def text_indentation(text):
    """
    Prints tokenized string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i - 1] == "." or text[i - 1] == ":" or text[i - 1] == "?":
            print('\n')

        print(text[i], end="")
