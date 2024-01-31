class Person:
    '''This is the blueprint of a person'''

    person_count = 0

    def __init__(self,name,dob,address):
        '''This is the constructor of an object'''
        self.name = name
        self.dob = dob
        self.address = address
        Person.inc_person_count()

    @staticmethod
    def inc_person_count():
        '''This will increase the person count'''
        Person.person_count += 1

    @staticmethod
    def get_person_count():
        '''This will return count of class attribute'''
        return Person.person_count

    def get_name(self):
        '''This will return name'''
        return self.name
    
    def get_dob(self):
        '''This will return dob'''
        return self.dob
    
    def get_address(self):
        '''This will return address'''
        return self.address
    
    def set_name(self,name):
        '''This will add new name in an object'''
        self.name = name

    def set_dob(self,dob):
        '''This will add new dob in an object'''
        self.dob = dob

    def set_address(self,address):
        '''This will add new address in an object'''
        self.address = address
    
    def __str__(self):
        '''Print function will know what to do'''
        return f'\nName: {self.name}\nDoB: {self.dob}\nAddress: {self.address}\n'
    
    def __del__(self):
        '''This will delete the instance or object of a class'''
        print('Deleted!!')
        Person.count -= 1
