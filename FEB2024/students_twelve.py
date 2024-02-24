'''This module for store students data'''

class Student:
    '''This is will create a object of students'''
    def __init__(self,roll_number,name,mark):
        '''This method initialize the class with roll_number, name and mark'''
        self.roll_number = roll_number
        self.name = name
        self.mark = mark
    
    def __str__(self):
        '''This will return the object of printable one'''
        return f'Roll Number: {self.roll_number}, Name: {self.name}, Mark: {self.mark}'
