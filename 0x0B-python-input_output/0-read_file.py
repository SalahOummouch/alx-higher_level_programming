#!/usr/bin/python3
'''0-read_file.py'''
def read_file(filename=""):
     '''function that reads a text file (UTF8) 
    Args:
        filname: file

    Returns:
        prints text to stdout
    '''
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
