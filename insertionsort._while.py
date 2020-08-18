# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:17:48 2020

@author: Aditya
"""

def insertion(A):
    for i in range(1,len(A)):
        j=i-1
        while j>=0:
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
            else:
                pass
            j-=1
            
A = [1,5,8,7,6]
insertion(A)
print(A)