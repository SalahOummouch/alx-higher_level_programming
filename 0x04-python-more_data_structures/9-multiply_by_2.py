#!/usr/bin/python3
# 9-multiply_by_2.py
def multiply_by_2(a_dictionary):
    '''Return a new dictionary with all values multiplied by 2.'''
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] *= 2
    return new_dict
