#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not type(roman_string) is str:
        return 0

    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0

    rev = roman_string[::-1]
    
    for i in range(len(rev)):
        if i != 0 and dict[rev[i - 1]] > dict[rev[i]]:
            number = number - dict[rev[i]]
        else:
            number = number + dict[rev[i]]
    return int(number)
