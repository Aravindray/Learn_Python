# This class is the derived class of person
import sys
sys.path.append('D:\\Github\\Python\\JAN2024')
from person import Person
from abc import abstractmethod

class Student(Person):
    '''This class will hold the student name, roll_number, standard, obtained_mark, years as a data attribute
    name - string from person
    roll_number, obtained_mark, year - numbers
    standard - string'''
    def __init__(self,name,roll_number,standard,obtained_mark,year):
        '''This is a class constructor'''
        super().__init__(name,None,None)
        self.roll_number = roll_number
        self.standard = standard
        self.obtained_mark = obtained_mark
        self.year = year

    @abstractmethod
    def percentage(self):
        '''This is the abstract method'''
        pass

    def __str__(self):
        '''This will print'''
        return f'Name: {self.name}\nRoll Number: {self.roll_number}\nClass: {self.standard}\nScored Mark: {self.obtained_mark}'

class Grade(Student):
    '''This is the derived class from Student'''
    total_mark = 600

    def __init__(self,name,roll_number,standard,obtained_mark,year):
        '''This is a class constructor'''
        if obtained_mark >= 0 and obtained_mark <= 600:
            super().__init__(name,roll_number,standard,obtained_mark,year)
        else:
            print('obtained mark is out of range')

    @staticmethod
    def get_total_mark():
        '''This will return total mark of class grade'''
        return Grade.total_mark

    def set_obtained_mark(self,new_marks):
        '''This will add new marks'''
        assert new_marks >= 0 and new_marks <= 600
        self.obtained_mark = new_marks

    def percentage(self):
        '''This will calculate percentage'''
        percent = (self.obtained_mark / Grade.get_total_mark()) * 100
        return round(percent,2)
    
    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nTotal Mark: {Grade.get_total_mark()}\nPercentage: {self.percentage()}'

class PostGrad(Student):
    '''This class is the derived class of Student'''
    total_mark = 400

    def __init__(self,name,roll_number,standard,obtained_mark,year):
        '''This is a class constructor'''
        if obtained_mark >= 0 and obtained_mark <= 400:
            super().__init__(name,roll_number,standard,obtained_mark,year)
        else:
            print('obtained mark is out of range')

    @staticmethod
    def get_total_mark():
        '''This will return total mark of class attribute'''
        return PostGrad.total_mark

    def set_obtained_mark(self,new_mark):
        '''This will update new mark'''
        assert new_mark >= 0 and new_mark <= 400
        self.obtained_mark = new_mark

    def percentage(self):
        '''This will calculate percentage'''
        percent = (self.obtained_mark / PostGrad.get_total_mark()) * 100
        return round(percent,2)
    
    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nTotal Mark: {PostGrad.get_total_mark()}\nPercentage: {self.percentage()}'


grade1 = Grade('Aravind',1001,'ECE',500,'2016')
print(grade1)
print()
postgrade1 = PostGrad('Dani',1002,'MECH',302,'2017')
print(postgrade1)
