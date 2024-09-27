'''Python Crash Course - Exercise 9 - Try it Yourself'''
# Author: Aravind Date: Thu, 26/9 2024

# 9-9

class Car:
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car's milage.'''
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increase_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles

class Battery:
    '''A simple attempt to model a battery for an electric car.'''

    def __init__(self, battery_size=40):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 40:
            mile_range = 150
        elif self.battery_size == 65:
            mile_range = 225

        print(f'This car can go about {mile_range} miles on a full charge.')

    def upgrade_battery(self):
        '''Upgrade the car's battery size'''
        self.battery_size = 65

class ElectricCar(Car):
    '''Represent aspect of a car, specific to the electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize an attribute of parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        '''Electric car doesn't have a gas tanks.'''
        print('This car doesn\'t have a gas tank!')

my_leaf = ElectricCar('Nissan', 'Leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
