#!/usr/bin/python3
"""
This is the "1-my_list" module.
The 1-my_list module supplies one function, my-list.
"""


class MyList(list):
    """Mylist class based upon list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        list = self.copy()
        print(sorted(list))
