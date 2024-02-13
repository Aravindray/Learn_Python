from abc import ABCMeta, abstractmethod
import math
class Shapes:
    '''This is a base abstract class for shapes to find area and perimeter'''
    __metaclass__ = ABCMeta
    def __init__(self,shape_type):
        '''This is a class constructor with share type as a argument'''
        self.shape_type = shape_type 
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shapes):
    '''This class will calculate area and perimeter for rectangle'''
    def __init__(self,name,length,breadth):
        '''This is a class constructor'''
        Shapes.__init__(self,name)
        self.length = length
        self.breadth = breadth
    
    def area(self):
        '''formula to find area of rectangle is length * breadth'''
        return self.length * self.breadth
    
    def perimeter(self):
        '''formula to find perimeter of rectangle is 2 * (length + breadth)'''
        return 2 * (self.length + self.breadth)
    
class Circle(Shapes):
    '''This class will calculate area and perimeter of circle'''
    def __init__(self,name,radius):
        Shapes.__init__(self,name)
        self.radius = radius

    def area(self):
        '''formula to find area of circle is pi * (r ** 2)'''
        return round(math.pi * (self.radius ** 2),3)
    
    def perimeter(self):
        '''formula to find perimeter of circle is 2 * pi * r'''
        return round(2 * math.pi * self.radius, 3)
