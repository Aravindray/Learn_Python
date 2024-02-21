# This is a class vehicle script

class Vehicle:
    '''This class store registration number, make, model and color as object attributes'''

    def __init__(self,reg_num,make,model,color):
        '''This will construct the class'''
        self.reg_num = reg_num
        self.make = make
        self.model = model
        self.color = color

    def get_reg_num(self):
        '''This method will return reg number of a vehicle'''
        return self.reg_num
    
    def get_make(self):
        '''This method will return make of a vehicle'''
        return self.make
    
    def get_model(self):
        '''This method will return model of a vehicle'''
        return self.model
    
    def get_color(self):
        '''This method will return model of a vehicle'''
        return self.color
    
    def set_reg_num(self,new_reg_num):
        '''This method will return reg number of a vehicle'''
        self.reg_num = new_reg_num
    
    def set_make(self,new_make):
        '''This method will return make of a vehicle'''
        self.make = new_make
    
    def set_model(self,new_model):
        '''This method will return model of a vehicle'''
        self.model = new_model
    
    def set_color(self,new_color):
        '''This method will return model of a vehicle'''
        self.color = new_color

    def __str__(self):
        '''This will print'''
        return f'Registration Number: {self.get_reg_num()}\nMake: {self.get_make()}\nModel: {self.get_model()}\nColor: {self.get_color()}'


class PassengerVehicle(Vehicle):
    '''This is the derived class of vehicle which hold maximum passenger capacity as additional object attribute'''

    def __init__(self,reg_num,make,model,color,passenger_capacity):
        '''This is class constructor'''
        super().__init__(reg_num,make,model,color)
        self.max_passenger_capacity = passenger_capacity

    def get_passenger_capacity(self):
        '''This will return passenger capacity'''
        return self.max_passenger_capacity
    
    def set_passenger_capacity(self, new_capacity):
        '''This will return passenger capacity'''
        self.max_passenger_capacity = new_capacity

    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nPassenger Capacity: {self.get_passenger_capacity()}'


class CommercialVehicle(Vehicle):
    '''This is the derived class of vehicle which hold maximum load capacity as additional object attribute'''

    def __init__(self,reg_num,make,model,color,load_capacity):
        '''This is class constructor'''
        super().__init__(reg_num,make,model,color)
        self.max_load_capacity = load_capacity

    def get_load_capacity(self):
        '''This will return passenger capacity'''
        return self.max_load_capacity
    
    def set_load_capacity(self, new_capacity):
        '''This will return passenger capacity'''
        self.max_load_capacity = new_capacity

    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nLoad Capacity: {self.get_load_capacity()}'


cv1 = CommercialVehicle(1,'what is make','what is model','white',1000)
print(cv1)
pv1 = PassengerVehicle(1,'what is make','what is model','black',50)
print(pv1)
