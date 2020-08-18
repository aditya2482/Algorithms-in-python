# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:22:25 2020

@author: Aditya
"""

def bubble_sort(array):
    n = len(array)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                
                
array = [5,3,2,1,4]
bubble_sort(array)
print(array)
                