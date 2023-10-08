#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        new_list = []
        for i in range(len(my_list)):
            new_list.append(my_list[i])
            if i == idx:
                new_list[i] = element
            else:
                new_list = my_list
    return new_list
