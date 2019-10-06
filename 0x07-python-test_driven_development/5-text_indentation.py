#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """text_indentation function
    Args:  text is the text to be printed
    Prints:  text """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    symbols = ['.', '?', ':']

    for i in range(len(text)):
        if (text[i] in symbols):
            string += text[i] + '\n\n'
        else:
            if (i != 0 and
                (text[i - 1] in symbols or text[i - 1] is ' ') and
               text[i] is ' '):
                    pass
            else:
                    string += text[i]

    print(string, end="")
