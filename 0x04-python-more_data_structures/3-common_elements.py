#!/usr/bin/python3
# 3. Present in both
def common_elements(set_1, set_2):
    '''function that returns a set of common elements in two sets.'''
    commont_elements = []
    for element1 in set_1:
        for element2 in set_2:
            if element1 == element2:
                commont_elements.append(element1)
    return commont_elements
