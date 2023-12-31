#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for i in my_list:
            if elements_printed < x:
                print(i, end="")
                elements_printed += 1
        print("")
    except Exception as e:
        pass
    return elements_printed
