#!/usr/bin/python3
'''0-read_file.py'''
def read_file(filename=""):
    '''Function that reads a text file (UTF8).
    
    Args:
        filename (str): The name of the file to be read.

    Returns:
        None

    Prints the text to stdout.
    '''

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

