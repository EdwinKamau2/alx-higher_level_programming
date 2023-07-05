#!/usr/bin/python3
"""
    is the text_indentation module
"""


def text_indentation(text):
    """ Indents text on . : or ? """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    output = ""
    for char in text:
        output += char
        if char in ".:?":
            output += "\n\n"

    lines = output.splitlines()
    indented_text = "\n".join(line.strip() for line in lines)
    print(indented_text, end="")
