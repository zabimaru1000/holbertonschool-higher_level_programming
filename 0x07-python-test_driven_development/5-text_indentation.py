#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i - 1] == "." or text[i - 1] == ":" or text[i - 1] == "?":
            print()

        print(text[i], end="")
