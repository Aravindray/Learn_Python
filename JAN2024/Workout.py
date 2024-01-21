class Person:
    '''This class is to store data about a person'''
    count = 0

    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address
        Person.count += 1

    def get_name(self):
        return self.name
    
    def get_dob(self):
        return self.dob
    
    def get_address(self):
        return self.address
    
    def get_count(self):
        return Person.count

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob
    
    def set_address(self, address):
        self.address = address

    def __str__(self):
        return f'Name:{self.name}, DOB:{self.dob}, address:{self.address}'
