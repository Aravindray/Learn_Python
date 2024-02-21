'''This is the derived class of Points'''
import sys
import math
from points import Points

class LineSegments(Points):
    '''This class will calculate distance and midpoint of a line segment'''

    def __init__(self,x1,y1,x2,y2):
        '''This is a class constructor'''
        super().__init__(x1,y1)
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        '''Distance formula D = √(x₂ - x₁) ** 2 + (y₂ - y₁) ** 2'''
        distance = math.sqrt((self.x2 - self.x)**2+(self.y2 - self.y)**2)
        return round(distance,2)

    def midpoint(self):
        '''Midpoint formula M = ((x₂ + x₁)/2,(y₂ + y₁)/2)'''
        midpoint_x = (self.x + self.x2) / 2
        midpoint_y = (self.y + self.y2) / 2
        return Points(midpoint_x, midpoint_y)
    
    def __str__(self):
        '''This will print'''
        return f'A{super().__str__()} B{Points(self.x2,self.y2)}'
    

AB = LineSegments(1,5,3,1)
print(AB)
print('Distance:',AB.distance())
print('Midpoint:',AB.midpoint())
