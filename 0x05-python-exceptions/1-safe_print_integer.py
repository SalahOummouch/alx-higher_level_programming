#!/usr/bin/python3
def safe_print_integer(value):
    try:
        new_value = int(value)
        print(new_value)
        return True
    except Exception as e:
        return False