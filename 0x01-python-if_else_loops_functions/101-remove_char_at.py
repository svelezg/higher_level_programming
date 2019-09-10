#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    copy = ''
    for character in str[:]:
        if i != n:
            copy = copy + character
        i = i + 1

    return copy
