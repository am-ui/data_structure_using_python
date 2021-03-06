# -*- coding: utf-8 -*-
"""matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EZii9kDNqjg4oBMGo_Y-Nt9xQF5JR6Lk

#Matrix
:- Matrix is a special case of two dimensional array where each data element is of strictly same size. So every matrix is also a two dimensional array but not vice versa
"""

from numpy import *

matrix=([['sunday', 1, 2, 3, 4, 5],
              ['monday', 6, 7, 8, 9, 10],
              ['tuesday', 11, 12, 13, 14, 15],
              ['wednesday', 16, 17, 18, 19, 20],
              ['thrusday', 21, 22, 23, 24, 25],
              ['friday', 26, 27, 28, 29, 30],
              ['satarday', 31, 32, 33, 34, 35]])

matrix

#Accessing the element of the matrix
matrix [2]

matrix [1][2]

#Adding a rows in matrix 
A_matrix = append(matrix, [['avg', 30, 35, 40, 45, 50]],0)

A_matrix [2]

#delete rows
bmatrix=delete(matrix,[2],0)

bmatrix

#delete column
bmatrix=delete(bmatrix,[2],1)

bmatrix

#update an rows 
matrix[3] = ['amit',0,0,0,0,0]

matrix

