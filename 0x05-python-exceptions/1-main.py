#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

import pycodestyle

def check_pep8_compliance(filename):
    style_guide = pycodestyle.StyleGuide()
    result = style_guide.check_files([filename])
    return result.total_errors

filename = "1-safe_print_integer.py"  # Remplacez par le nom de votre fichier
num_errors = check_pep8_compliance(filename)

if num_errors == 0:
    print(f"The code in {filename} is PEP 8 compliant.")
else:
    print(f"{num_errors} PEP 8 violations found in {filename}.")
