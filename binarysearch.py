#, -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:34:12 2020

@author: Aditya
"""
def binary(array,k):
    for i in range(0,len(array)):
        if array[i]==k:
            return True
        else:
            pass

array= [1,2,5,7,9]
print(binary(array,2))
