#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst_ord = list(a_dictionary.keys())
    lst_ord.sort()
    for i in lst_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
