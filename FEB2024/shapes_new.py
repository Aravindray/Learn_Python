'''This is a exercise module'''
from abc import ABCMeta, abstractmethod
import math

class Shapes:
    '''This is a abstract class'''
    __metaclass__ = ABCMeta
    def __init__(self,shapeType,x,y):
        self.shapeType = shapeType
        self.x = x
        self.y = y

    def compute_area():
        '''This is a abstract method'''
        pass


class Rectangle(Shapes):
    '''This class will calculate area'''
    def __init__(self,width,height):
        '''This is a class constructor'''
        Shapes.__init__(self,'Rectangle',width,height)

    def compute_area(self):
        '''This will calculate area of rectangle'''
        area = self.x * self.y
        return area
    
class Triangle(Shapes):
    '''This class will calculate area of triangle'''

    def __init__(self,height,base):
        '''This is a class constructor'''
        Shapes.__init__(self,'Triangle',height,base)

    def compute_area(self):
        '''This will calculate area of Triangle'''
        area = 0.5 * self.x * self.y
        return area
    
    
r1 = Rectangle(12,12)
t1 = Triangle(4,3)
print(r1.compute_area())
print(type(r1.compute_area()))
print(t1.compute_area())
print(type(t1.compute_area()))
