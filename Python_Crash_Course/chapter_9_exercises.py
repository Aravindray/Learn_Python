# Author: Aravind Date: Thu, 26/9 2024

# 9-1
class Restaurant:
    '''
    Objective: Stores about restaurant_name and cuisine_type
    '''
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        '''Class Constructor'''
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type
