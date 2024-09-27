'''Python Crash Course - Exercise 9 - Try it Yourself'''
# Author: Aravind Date: Thu, 26/9 2024

# 9-1, 9-3, 9-4
class Restaurant:
    '''
    Objective: Stores about restaurant_name and cuisine_type
    '''
    number_served = 0

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        '''Class Constructor'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''It describes about restaurant'''
        print(f'\nName: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}')

    def open_restaurant(self):
        '''Restaurant is always open'''
        print(f'{self.restaurant_name} is now open.')

    def set_number_served(self, customers_count):
        '''Add the new customer counts'''
        self.number_served = customers_count

    def increment_number_served(self, new_customers_count):
        '''Increase the number count with given count'''
        self.number_served += new_customers_count

restaurant1 = Restaurant('Le Bistro Du Parc', 'French')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
 
restaurant2 = Restaurant('Chicago Curry House', 'Indian & Nepalese')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('McDonald\'s','American')
restaurant3.describe_restaurant()

print(restaurant1.number_served)
restaurant1.number_served = 1
print(restaurant1.number_served)

print(restaurant2.number_served)
restaurant2.set_number_served(3)
print(restaurant2.number_served)

restaurant3.set_number_served(5)
print(restaurant3.number_served)
restaurant3.increment_number_served(3)
print(restaurant3.number_served)

# 9-6
class IceCreamStand(Restaurant):
    '''An extended version of Restaurant'''
    flavors = ['Vanilla',
               'Strawberry',
               'Chocolate',
               'Blueberry',
               'Mint Chocolate Chip',
               'Cookies and Cream',
               'Butter Pecan',
               'Mango',
               'Cotton Candy']

    def display_flavors(self):
        '''Will display all flavors'''
        print('We have')
        for flavor in self.flavors:
            print(f'- {flavor.title()} Ice Cream')

ic = IceCreamStand("Angel's Ice Cream", 'American')
ic.describe_restaurant()
ic.flavors.append('Coffee')
ic.display_flavors()
