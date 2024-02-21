# This is the derived class of passenger vehicle
from vehicle import PassengerVehicle
import sys

class Car(PassengerVehicle):
    '''This class have no of doors as object attribute'''
    def __init__(self,reg_num,make,model,color,passenger_capacity,no_of_doors):
        '''This is class constructor'''
        super().__init__(reg_num,make,model,color,passenger_capacity)
        self.no_of_doors = no_of_doors
    
    def get_no_of_doors(self):
        '''This will return no of doors'''
        return self.no_of_doors
    
    def set_no_of_doors(self,new_doors):
        '''This will new no of doors'''
        self.no_of_doors = new_doors

    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nNo of Doors: {self.get_no_of_doors()}'

class Bus(PassengerVehicle):
    '''This class have no of doors as object attribute and double_decker as boolean'''
    def __init__(self,reg_num,make,model,color,passenger_capacity,no_of_doors,double_decker):
        '''This is a class constructor'''
        super().__init__(reg_num,make,model,color,passenger_capacity)
        self.no_of_doors = no_of_doors
        if isinstance(double_decker,bool):
            self.double_decker = double_decker
        else:
            print('Double decker should be either True or False boolean variables')
            sys.exit()
    
    def get_no_of_doors(self):
        '''This will return no of doors'''
        return self.no_of_doors
    
    def set_no_of_doors(self,new_doors):
        '''This will new no of doors'''
        self.no_of_doors = new_doors

    def get_double_decker(self):
        '''This will return the status of double decker'''
        return self.double_decker
    
    def set_double_decker(self,new_status):
        '''This method will update the status'''
        self.double_decker = new_status
    
    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nNo of Doors: {self.get_no_of_doors()}\nDouble Decker: {self.get_double_decker()}'

class Autorickshaw(PassengerVehicle):
    pass

c1 = Car(123,'Ford','Fusion','White',4,4)
print(c1)
print()
b1 = Bus(345,'BMW','S1','Green',50,4,False)
print(b1)
print()
a1 = Autorickshaw(231,'TVS','Deluxe','Yellow',6)
print(a1)
