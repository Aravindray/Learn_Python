'''This module is the implementation of stack with similar of linked list'''
from node import Node

class LinkedStack:
    '''This class add or delete element is top of the stack'''
    def __init__(self):
        '''class initialize with empty top element'''
        self.top = None
    
    def push(self, value):
        '''Push the new element in top of the stack'''
        if self.top is None:
            self.top = Node(value)
            print('value added')
        else:
            temp = Node(value)
            temp.next = self.top
            self.top = temp
            print('value added')

    def pop(self):
        '''Delete the top element from the stack'''
        if self.top is None:
            print('Stack underflow!')
            return None
        else:
            temp = self.top
            value = temp.data
            self.top = self.top.next
            del temp
            print('Top value is deleted')
            return value


    def __str__(self):
        '''The stack with be represented as [x]y]z]'''
        result = '['
        current = self.top
        while current.next is not None:
            result += str(current.data) + '['
            current = current.next
        result += str(current.data) + ']'
        return result
