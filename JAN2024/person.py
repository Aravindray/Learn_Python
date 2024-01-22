class Person:
    '''This class is to store data about a person'''
    count = 0

    def __init__(self, name, dob, address):
        '''This method will add data attributes of a class Person for an object'''
        self.name = name
        self.dob = dob
        self.address = address
        Person.count += 1

    def get_name(self):
        '''This method will return name of the object'''
        return self.name
    
    def get_dob(self):
        '''This method will return DOB (Date of Birth) of the object'''
        return self.dob
    
    def get_address(self):
        '''This method will return address of the object'''
        return self.address
    
    def get_count(self):
        '''This method will return count of class Person variable'''
        return Person.count

    def set_name(self, name):
        '''This method will assign new name of the object'''
        self.name = name

    def set_dob(self, dob):
        '''This method will assign new DOB (Date of Birth) of the object'''
        self.dob = dob
    
    def set_address(self, address):
        '''This method will assign new address of the object'''
        self.address = address

    def __str__(self):
        '''This method will help print object data'''
        return f'Name: {self.name},\nDOB: {self.dob},\naddress: {self.address}\n'
    
    def __del__(self):
        '''This method will delete the instance of the class'''
        Person.count -= 1
        print('Deleted!')
