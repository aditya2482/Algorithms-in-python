# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:16:44 2020

@author: Aditya
"""

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def getgrade(self,grade):
        self.grade = grade
        
class course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_grade(self):
        value = 0
        for student in self.students:
            value = student.getgrade()
            
        return value/len(self.students)
            
    
s1 = Student("aditya",20,95)
s2 = Student("roma",19,99)
s3 = Student("praveen",20,95)

c = course("science",2)
c.add_student(s1)
c.add_student(s2)

print(c.students[0].name)