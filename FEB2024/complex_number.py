# This is the script of complex number
import sys

class ComplexNumber:
    '''This class have +, -, and * operator overloading'''
    def __init__(self,real=0,imaginary=0):
        '''This method have real and imaginary attributes as number'''
        self.real = real
        self.imaginary = imaginary

    def __add__(self,other):
        '''This method add the 2 complex number'''
        if isinstance(other,ComplexNumber):
            real_part = self.real + other.real
            imaginary_part = self.imaginary + other.imaginary
            return ComplexNumber(real_part,imaginary_part)
        print('Both must be same data type')
        sys.exit()

    def __sub__(self,other):
        '''This method subtract the 2 complex number'''
        if isinstance(other,ComplexNumber):
            real_part = self.real - other.real
            imaginary_part = self.imaginary - other.imaginary
            return ComplexNumber(real_part,imaginary_part)
        print('Both must be same data type')
        sys.exit()

    def __mul__(self,other):
        if isinstance(other,ComplexNumber):
            real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
            imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
            return ComplexNumber(real_part,imaginary_part)
        print('Both must be same data type')
        sys.exit()
    
    def __str__(self):
        '''This will print the complex number in this format a + ib'''
        if self.imaginary < 0:
            return f'{self.real}{self.imaginary}i'
        
        return f'{self.real}+{self.imaginary}i'
