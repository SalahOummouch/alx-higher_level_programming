#!/usr/bin/python3
import pycodestyle
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

def check_pep8_compliance(filename):
    style_guide = pycodestyle.StyleGuide()
    result = style_guide.check_files([filename])
    return result.total_errors

filename = "0-square_matrix_simple.py"  # Nom du fichier
num_errors = check_pep8_compliance(filename)

if num_errors == 0:
    print(f"The code in {filename} is PEP 8 compliant.")
else:
    print(f"{num_errors} PEP 8 violations found in {filename}.")

