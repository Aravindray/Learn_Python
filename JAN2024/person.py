'''This is a module for person'''
from my_date import MyDate

class Person:
    '''This class is the blueprint of person'''

    person_count = 0

    def __init__(self,name,dob,address):
        '''This is a class constructor'''
        self.name = name
        self.dob = dob
        self.address = address
        Person.inc_person_count()

    @staticmethod
    def inc_person_count():
        '''This will increase the count of class attribute person_count'''
        Person.person_count += 1
    
    @staticmethod
    def get_person_count():
        '''This will return the class attribute person count'''
        return Person.person_count
    
    @staticmethod
    def dec_person_count():
        '''This will decrease the count of the class attribute person_count'''
        Person.person_count -= 1
    
    def get_name(self):
        '''This will return object attribute name'''
        return self.name
    
    def get_dob(self):
        '''This will return object attribute dob'''
        return self.dob
    
    def get_address(self):
        '''This will return object attribute address'''
        return self.address
    
    def set_name(self,new_name):
        '''This will update new name of object attribute name'''
        self.name = new_name

    def set_dob(self,new_dob):
        '''This will update new dob of object attribute dob'''
        self.dob = new_dob

    def set_address(self,new_address):
        '''This will update new address of object attribute address'''
        self.address = new_address

    def __str__(self):
        '''This will print'''
        return f'Name: {self.name}\nDOB: {self.dob}\nAddress: {self.address}\n'
    
    def __del__(self):
        '''This will return Deleted!! when an class object was be deleted'''
        print('Deleted!!')
        Person.dec_person_count()
