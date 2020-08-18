# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:49:55 2020

@author: Aditya
"""

def bubble_sort(array):
    for i in range(1,len(array)):
        j = i+1
        while(j>=0):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            else:
                pass
            
array = [5,3,2,1,4]
bubble_sort(array)
print(array)
                