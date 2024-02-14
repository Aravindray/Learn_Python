'''This module is for calculate line segments distance and midpoint'''
from points import Points
import sys
import math

class LineSegments:
    '''This class will calculate distance and midpoint'''

    def __init__(self,A,B):
        '''This is class constructor'''
        if isinstance(A,Points) and isinstance(B,Points):
            self.A = A
            self.B = B
        else:
            print('Instance must be points type')
            sys.exit()
        
    def distance(self):
        '''formula to find distance is sqrt((x2 - x1)**2 + (y2 - y1)**2)'''
        distance = math.sqrt((self.B.get_x() - self.A.get_x())**2 + (self.B.get_y() - self.A.get_y())**2)
        return f'Distance is {distance}'
    
    def midpoint(self):
        '''formula to find midpoint is ((x1,x2)/2,(y1,y2)/2)'''
        midpoint_x = (self.A.get_x() + self.B.get_x()) / 2
        midpoint_y = (self.A.get_y() + self.B.get_y()) / 2
        return f'Midpoint is ({midpoint_x},{midpoint_y})'


O = Points(3,5)
P = Points(2,1)
OP = LineSegments(O,P)
print(OP.distance())
print(OP.midpoint())
