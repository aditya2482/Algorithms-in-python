# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:41:40 2020

@author: Aditya
"""


def quicksort(array):
    quick_sort(array,0,len(array)-1)
    
def quick_sort(array,low,high):
    if low<high:
        pivot = partition(array,low,high)
        quick_sort(array,low,pivot-1)
        quick_sort(array,pivot+1,high)
        
def get_pivot(array,low,high):
    middle = (low+high)//2
    pivot = high
    if array[low]<array[middle]:
        if array[middle]<array[high]:
            pivot = middle
    elif array[low]<array[high]:
        pivot = low
    return (pivot)
    
def partition(array,low,high):
    pivot_index = get_pivot(array,low,high)
    pivot_value = array[pivot_index]
    array[pivot_index],array[low]=array[low],array[pivot_index]
    border = low
    
    for i in range(low,high):
        if array[i]<pivot_value:
            border+=1
            array[border],array[i]=array[i],array[border]
        array[low],array[border]=array[border],array[low]
        
    return(border)
    
array = [1,8,7,6]
quicksort(array)
print(array)
