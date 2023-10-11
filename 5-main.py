#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
import pycodestyle

def check_pep8_compliance(filename):
    style_guide = pycodestyle.StyleGuide()
    result = style_guide.check_files([filename])
    return result.total_errors

filename = "5-number_keys.py"  # Nom du fichier
num_errors = check_pep8_compliance(filename)

if num_errors == 0:
    print(f"The code in {filename} is PEP 8 compliant.")
else:
    print(f"{num_errors} PEP 8 violations found in {filename}.")

