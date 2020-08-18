# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:08:13 2020

@author: Aditya
"""

class stacks:
    def __init__(self):
        self.items = []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
        
s = stacks()
s.push("a")
s.push("b")
print(s.get_stack())
s.pop()
print(s.get_stack())