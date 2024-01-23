# Calsses I

**Exercises**

Question 1: 

    import sys

    class Rectangle:
        '''
        Objective: Class Rectangle is used to find the area and perimeter of the rectangle as per the user input
        Input: Length & Breadth - Float
        Output: Area & Perimeter - Float
        '''
        def __init__(self, length, breadth):
            '''Initialization the class and assign length and breadth respectively to the object'''
            if length > 0 and breadth > 0:
                self.length = length
                self.breadth = breadth
            else:
                print('Length or breadth should be greater than zero')
                sys.exit()

        def set_length(self, length):
            '''Update the new length'''
            if length > 0:
                self.length = length
            else:
                print('Length should be greater than zero')
                sys.exit()

        def set_breadth(self, breadth):
            '''Update the new breadth'''
            if breadth > 0:
                self.breadth = breadth
            else:
                print('Breadth should be greater than zero')
                sys.exit()

        def get_length(self):
            '''Return the length'''
            return self.length
        
        def get_breadth(self):
            '''Return the breadth'''
            return self.breadth
        
        def area(self):
            '''Find the area of the rectangle'''
            return self.length * self.breadth

        def perimeter(self):
            '''Find the area of the perimeter'''
            return 2 * (self.length + self.breadth)

        def __str__(self):
            '''You know what __str__ function do'''
            return f'Area of the given length {self.length} and breadth {self.breadth} is {self.area()} and Perimeter of the given length {self.length} and breadth {self.breadth} is {self.perimeter()}'

    def main():
        '''This is a main function'''
        length = float(input('Enter the length of the rectangle: '))
        breadth = float(input('Enter the breadth of the rectangle: '))

        result = Rectangle(length, breadth)
        print(result)

    if __name__ == '__main__':
        main()


Question 2: 
