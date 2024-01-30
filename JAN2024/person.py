class Person:
    '''This is the blueprint of a person'''

    count = 0

    def __init__(self,name,dob,address):
        '''This is the constructor of an object'''
        self.name = name
        self.dob = dob
        self.address = address
        Person.count += 1

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

    def get_count(self):
        '''This will return count of class attribute'''
        return Person.count
    
    def __str__(self):
        '''Print function will know what to do'''
        return f'\nName: {self.name}\nDoB: {self.dob}\nAddress: {self.address}\n'
    
    def __del__(self):
        '''This will delete the instance or object of a class'''
        print('Deleted!!')
        Person.count -= 1
    
p1 = Person('Aravindraj','15-05-1999','AG Street, Vazhapadi')
print(p1)
p2 = Person('Not Aravindraj','not 15-05-1999','Not Vazhapadi')
p2.set_dob('16-05-1999')
print(p2)
