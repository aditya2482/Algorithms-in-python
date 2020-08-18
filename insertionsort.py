# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:29:33 2020

@author: Aditya
"""

def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i-1,0,-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            else:
                break
            
    
array = [1,5,7,4,6,59,6]
insertion_sort(array)
print(array)