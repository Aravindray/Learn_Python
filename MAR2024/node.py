'''This is the primary module for linked list which hold node class'''

class Node:
    '''This class is part of the linked list which contain a object of node'''
    def __init__(self, value):
        '''This method contain value and next attribute'''
        self.data = value
        self.next = None

    def __str__(self):
        '''This method return string format of value and next'''
        return f'{self.data}:{self.next}'


class DoubleNode:
    '''This class is will hold the two way communication of node'''
    def __init__(self, value):
        '''This method contain value, previous and next attributes'''
        self.previous = None
        self.data = value
        self.next = None

    def __str__(self):
        '''The structure of print will be Prev:Data:Next'''
        return f'{self.previous}:{self.data}:{self.next}'

class TreeNode:
    '''This class hold the left and right nodes of the root node'''
    def __init__(self, value):
        '''Object will constructed with left, data and right attributes'''
        self.left = None
        self.data = value
        self.right = None
    
    def __str__(self):
        '''The structure of print will be Left→Data←Right'''
        return f'{self.left}→{self.data}←{self.right}'
