#!/usr/bin/python3
# 4. Only differents
def only_diff_elements(set_1, set_2):
    '''function that returns a set of all elements present in only one set'''
    diff_elements = []
    for element1 in set_1:
        if element1 not in set_2:
            diff_elements.append(element1)
    for element2 in set_2:
        if element2 not in set_1:
            diff_elements.append(element2)
    return diff_elements
