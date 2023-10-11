#!/usr/bin/python3
# 2. Unique addition
def uniq_add(my_list=[]):
    ''' function that adds all unique integers in a list
    (only once for each integer).'''
    resultat = 0
    integers = []
    for i in my_list:
        exist = False
        for j in integers:
            if i == j:
                exist = True
        if not exist:
            integers.append(i)
            resultat += int(i)
    return resultat
