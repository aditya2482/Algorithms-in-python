# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:02:55 2020

@author: Aditya
"""

rows = int(input())
col = int(input())
matrix=[]
for i in range(rows):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)
    
for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
        
        

for i in range(rows):
    for j in range(col):
        if i == j:
            print(matrix[i][j],end=" ")
        else:
            pass
    
