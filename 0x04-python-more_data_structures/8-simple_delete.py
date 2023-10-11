#!/usr/bin/python3
# 8. Simple delete by key
def simple_delete(a_dictionary, key=""):
    '''function that deletes a key in a dictionary.'''
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
