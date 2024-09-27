# Author: Aravind Date: Thu, 26/9 2024
"""
# 9-1, 9-3
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
"""
# 9-2
class User:
    '''Stores about a user'''
    login_attempt = 0

    def __init__(self, first_name: str,
                 last_name: str,
                 email: str,
                 dob: str) -> None:
        '''Class Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob
    
    def describe_user(self):
        '''Describe about the user'''
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}"
              f"\nEmail: {self.email}\nDOB: {self.dob}")

    def greet_user(self):
        '''Greet user with Hello'''
        print(f'Hello {self.first_name.title()} {self.last_name.title()}!')
    
    def increment_login_attempt(self):
        '''Increase the class attribute by 1'''
        self.login_attempt += 1
    
    def reset_login_attempt(self):
        '''Reset the login attempt to 0'''
        self.login_attempt = 0

u1 = User('aravind', 'ray', 'admin@admin.com', '23-12-2004')
u2 = User('rock', 'star', 'rock@admin.com', '18-04-2010')
u3 = User('daniel', '', 'nothing@nothing.admin', '06-08-2005')

u1.describe_user()
u1.greet_user()

u2.describe_user()
u2.greet_user()

u3.describe_user()
u3.greet_user()

print(u1.login_attempt)
u1.increment_login_attempt()
u1.increment_login_attempt()
u1.increment_login_attempt()
print(u1.login_attempt)
u1.reset_login_attempt()
print(u1.login_attempt)
