# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:30:23 2020

@author: Aditya
"""
        
def iterative_1(array,target,low,high):
    if low > high:
        return False
    else:
        middle = (low+high)//2
        value = array[middle]
        if target == value:
            print("True")
        elif target<value:
            iterative_1(array,target,low,middle-1)
        else:
            iterative_1(array,target,middle+1,high)

array = [1,5,7,9,8,10]
print(iterative_1(array,1,0,len(array)-1))


        