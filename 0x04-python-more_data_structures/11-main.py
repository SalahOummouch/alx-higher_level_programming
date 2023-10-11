#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

import pycodestyle

def check_pep8_compliance(filename):
    style_guide = pycodestyle.StyleGuide()
    result = style_guide.check_files([filename])
    return result.total_errors

filename = "11-multiply_list_map.py"  # Nom du fichier
num_errors = check_pep8_compliance(filename)

if num_errors == 0:
    print(f"The code in {filename} is PEP 8 compliant.")
else:
    print(f"{num_errors} PEP 8 violations found in {filename}.")

