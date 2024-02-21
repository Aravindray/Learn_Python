'''This module is a coordinate of point x and y'''

class Points:
    '''This class is contain the coordinate points'''

    def __init__(self,x,y):
        '''This is a class constructor'''
        self.x = x
        self.y = y
    
    def get_x(self):
        '''This will return x'''
        return self.x
    
    def get_y(self):
        '''This will return y'''
        return self.y
    
    def set_x(self,new_x):
        '''This will add new x point'''
        self.x = new_x
    
    def set_y(self,new_y):
        '''This will add new y point'''
        self.x = new_y
    
    def __str__(self):
        '''This will print'''
        return f'({self.x}, {self.y})'
