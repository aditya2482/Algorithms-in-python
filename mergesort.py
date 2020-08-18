# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:18:48 2020

@author: Aditya
"""
def mergesort(array):
    merge_sort(array,0,len(array)-1)
    
def merge_sort(array,first,last):
    if first<last:
        middle = (first+last)//2
        merge_sort(array,first,middle)
        merge_sort(array,middle+1,last)
        merge(array,first,middle,last)
    
def merge(array,first,middle,last):
    left = array[first:middle]
    right = array[middle:last+1]
    left.append(999999999)
    right.append(999999999)
    i=j=0
    for k in range(first,last+1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1

array = [1,2,3,4,8,7]
mergesort(array)
print(array)
