#!/usr/bin/python3
"""is class MyList that inherits from list"""


class MyList(list):
    """this inherits from list"""
    def print_sorted(self):
        """this prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
