#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    j = 0
    for i in range(len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            new_string += my_string[i]
            j += 1
    return new_string

