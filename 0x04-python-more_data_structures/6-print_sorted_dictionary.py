#!/usr/bin/python3
# 6. Print sorted dictionary
def print_sorted_dictionary(a_dictionary):
    '''function that prints a dictionary by ordered keys.'''
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
