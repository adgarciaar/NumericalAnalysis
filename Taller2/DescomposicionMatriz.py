# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 08:02:35 2018

@author: Juanda
"""
import time
matrix = [[4,  -1,  -1, 0, 0],
          [6, 7,  8, 9, 10],
          [11, 12, 13, 14 , 15],
          [16, 17, 18 ,19 , 20],
          [21, 22, 23 ,24 , 25]]
inferior = [[0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0]]
superior = [[0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0]]
diagonal = [[0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0],
          [0,  0,  0, 0, 0]]

def TriangularInferior(matrix):
    starttime = time.time()
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix)):
            if j<=i:
                inferior[i][j] = matrix[i][j]
            else:
                inferior[i][j] = 0
    endtime = time.time() - starttime
    print ("El tiempo de ejecucion fue : ", endtime,'sg')
    return inferior
def TriangularSuperior(matrix):
    starttime = time.time()
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix)):
            if j>=i:
                superior[i][j] = matrix[i][j]
            else:
                superior[i][j] = 0
    endtime = time.time() - starttime
    print ("El tiempo de ejecucion fue : ", endtime,'sg')
    return superior
def Diagonal(matrix):
    starttime = time.time()
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix)):
            if j==i:
                diagonal[i][j] = matrix[i][j]
            else:
                diagonal[i][j] = 0
    endtime = time.time() - starttime
    print ("El tiempo de ejecucion fue : ", endtime,'sg')
    return diagonal

print()
print ('Inferior')
print(TriangularInferior(matrix))
print ('Superior')
print(TriangularSuperior(matrix))
print ('Diagonal')
print(Diagonal(matrix))

    
