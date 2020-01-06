#!/usr/bin/python3
"""
contains find_peak
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """

    if len(list_of_integers) > 0:

        # Base case 1
        if len(list_of_integers) == 1:
            return list_of_integers[0]

        # real floor division range split
        center = len(list_of_integers) // 2

        # Base case 2
        if len(list_of_integers) == 2:
            if list_of_integers[center] > list_of_integers[0]:
                return list_of_integers[center]
            else:
                return list_of_integers[0]

        # Base case 3
        if (list_of_integers[center] > list_of_integers[center + 1] and
                list_of_integers[center] > list_of_integers[center - 1]):
            return list_of_integers[center]

        # Recursive case 1 (Select left side from center)
        if list_of_integers[center - 1] > list_of_integers[center]:
            return find_peak(list_of_integers[0:center])

        # Recursive case 2 (Select right side from center)
        return find_peak(list_of_integers[center + 1:])
