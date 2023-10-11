#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
import pycodestyle

def check_pep8_compliance(filename):
    style_guide = pycodestyle.StyleGuide()
    result = style_guide.check_files([filename])
    return result.total_errors

filename = "3-common_elements.py"  # Nom du fichier
num_errors = check_pep8_compliance(filename)

if num_errors == 0:
    print(f"The code in {filename} is PEP 8 compliant.")
else:
    print(f"{num_errors} PEP 8 violations found in {filename}.")

