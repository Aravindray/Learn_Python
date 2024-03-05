'''This is the primary module for linked list which hold node class'''

class Node:
    '''This class is part of the linked list which contain a object of node'''
    def __init__(self,value):
        '''This method contain value and next attribute'''
        self.data = value
        self.next = None

    def __str__(self):
        '''This method return string format of value and next'''
        return f'{self.data}:{self.next}'
