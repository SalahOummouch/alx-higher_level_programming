#!/usr/bin/python3
# 0. Squared simple
def square_matrix_simple(matrix=[]):
    '''function that computes the square value of all integers of a matrix.''' 
    return [[x ** 2 for x in row] for row in matrix]

