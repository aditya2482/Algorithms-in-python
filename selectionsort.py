# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:45:07 2020

@author: Aditya
"""
min = 0

def selection_sort(array):
    for i in range (0,len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index = j
        if min_index != i:
            array[i],array[min_index]=array[min_index],array[i]
            

array = [1,8,7,6,6,2]
selection_sort(array)
print(array)
    