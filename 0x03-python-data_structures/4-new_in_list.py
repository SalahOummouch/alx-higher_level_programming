#!/usr/bin/python3
# 4-new_in_list.py
def new_in_list(my_list, idx, element):
    '''function that replaces an element in a list at a specific position without modifying the original list'''
    if idx >= 0 and idx < len(my_list):
        new_list = []
        for i in range(len(my_list)):
            new_list.append(my_list[i])
            if i == idx:
                new_list[i] = element
            else:
                new_list = my_list
    return new_list
